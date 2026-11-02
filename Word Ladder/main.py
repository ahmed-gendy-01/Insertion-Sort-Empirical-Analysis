from collections import deque, defaultdict
import matplotlib.pyplot as plt
import networkx as nx

# Milestone 1: Group words by length
def group_words_by_length(word_list):
    grouped = defaultdict(list)
    for word in word_list:
        grouped[len(word)].append(word)
    return grouped

# Helper: Check if two words differ by exactly 1 letter
def differ_by_one(w1, w2):
    if len(w1) != len(w2):
        return False
    diff = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

# Milestone 2: Connect words with an edge if they differ by 1 letter
def build_graph(words):
    adj = defaultdict(list)
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if differ_by_one(words[i], words[j]):
                adj[words[i]].append(words[j])
                adj[words[j]].append(words[i])
    return adj

# Milestone 3 & 4: Run BFS to find shortest path & reconstruct the ladder
def find_word_ladder(start_word, target_word, word_list):
    if len(start_word) != len(target_word):
        return None, None
    
    # Filter dictionary words with same length
    valid_words = [w for w in word_list if len(w) == len(start_word)]
    if start_word not in valid_words:
        valid_words.append(start_word)
    if target_word not in valid_words:
        valid_words.append(target_word)
        
    adj = build_graph(valid_words)
    
    queue = deque([start_word])
    visited = {start_word: None}  # word: parent
    
    found = False
    while queue:
        curr = queue.popleft()
        if curr == target_word:
            found = True
            break
            
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited[neighbor] = curr
                queue.append(neighbor)
                
    if not found:
        return None, adj
        
    # Reconstruct path
    path = []
    curr = target_word
    while curr is not None:
        path.append(curr)
        curr = visited[curr]
    path.reverse()
    
    return path, adj

# Plotting the Graph and Highlighting the Ladder
def plot_word_ladder_graph(adj, path, filename='word_ladder_graph.png'):
    G = nx.Graph()
    for node, neighbors in adj.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
            
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    
    path_edges = list(zip(path[:-1], path[1:])) if path else []
    
    node_colors = []
    for node in G.nodes():
        if path and node in path:
            if node == path[0] or node == path[-1]:
                node_colors.append('#2ecc71')  # Start/Target (Green)
            else:
                node_colors.append('#e74c3c')  # Path Nodes (Red)
        else:
            node_colors.append('#3498db')  # Other Nodes (Blue)
            
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1800)
    nx.draw_networkx_labels(G, pos, font_size=11, font_color='white', font_weight='bold')
    
    non_path_edges = [e for e in G.edges() if e not in path_edges and (e[1], e[0]) not in path_edges]
    nx.draw_networkx_edges(G, pos, edgelist=non_path_edges, edge_color='#bdc3c7', width=1.5)
    
    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='#e74c3c', width=3.5)
        
    plt.title(f"Word Ladder BFS Path: {' -> '.join(path)}", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

if __name__ == '__main__':
    # Words list matching slide example
    word_dictionary = ["hit", "hot", "dot", "dog", "lot", "log", "cog", "hat", "cat"]
    start = "hit"
    target = "cog"
    
    print(f"Finding Word Ladder: '{start}' -> '{target}'")
    ladder, graph = find_word_ladder(start, target, word_dictionary)
    
    if ladder:
        print("\nShortest Ladder Found:")
        print(" -> ".join(ladder))
        print(f"Steps: {len(ladder)} words ({len(ladder)-1} transitions)")
        plot_word_ladder_graph(graph, ladder)
    else:
        print("No valid ladder exists between these words.")