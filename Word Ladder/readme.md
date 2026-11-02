# Word Ladder Project (BFS Graph Implementation)

An implementation of the **Word Ladder** algorithm using **Breadth-First Search (BFS)** on an unweighted graph, developed for the *Analysis of Algorithms* course.

## Project Overview
- **Goal:** Transform a start word into a target word by changing one letter at a time, using valid dictionary words.
- **Graph Representation:**
  - **Vertices:** Words of identical length.
  - **Edges:** Connections between words differing by exactly one character.
- **Algorithm:** BFS guarantees finding the shortest transformation sequence.

## Example
- **Start Word:** `hit`
- **Target Word:** `cog`
- **Path:** `hit` -> `hot` -> `dot` -> `dog` -> `cog` (5 words, 4 changes)

## Output Graph
The generated `word_ladder_graph.png` visualizes the graph layout and highlights the shortest path in red.

## How to Run
```bash
pip install networkx matplotlib
python main.py