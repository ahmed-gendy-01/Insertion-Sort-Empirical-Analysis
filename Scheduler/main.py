import random
import time
import heapq
import matplotlib.pyplot as plt

# 1. Define Task Structure
class Task:
    def __init__(self, name, priority, arrival_time):
        self.name = name
        self.priority = priority
        self.arrival_time = arrival_time

    def __repr__(self):
        return f"[{self.name} | Priority: {self.priority}]"


# 2. Custom Max-Heap Implementation
class CustomMaxHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i): return (i - 1) // 2
    def _left_child(self, i): return 2 * i + 1
    def _right_child(self, i): return 2 * i + 2

    def _sift_up(self, i):
        while i > 0 and self.heap[i].priority > self.heap[self._parent(i)].priority:
            p = self._parent(i)
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p

    def _sift_down(self, i):
        max_idx = i
        left, right = self._left_child(i), self._right_child(i)
        n = len(self.heap)

        if left < n and self.heap[left].priority > self.heap[max_idx].priority:
            max_idx = left
        if right < n and self.heap[right].priority > self.heap[max_idx].priority:
            max_idx = right

        if i != max_idx:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self._sift_down(max_idx)

    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        max_task = self.heap[0]
        last_task = self.heap.pop()
        if self.heap:
            self.heap[0] = last_task
            self._sift_down(0)
        return max_task

    def is_empty(self):
        return len(self.heap) == 0


# 3. Simulation & Benchmark with Plotting
def run_benchmark_and_plot():
    sizes = [10000, 30000, 50000, 80000, 100000]
    custom_times = []
    builtin_times = []

    print("Running performance benchmark...")

    for num_tasks in sizes:
        test_tasks = [Task(f"T{i}", random.randint(1, 1000), 0) for i in range(num_tasks)]

        # Benchmark Custom Max-Heap
        custom_heap = CustomMaxHeap()
        t0 = time.perf_counter()
        for task in test_tasks:
            custom_heap.insert(task)
        while not custom_heap.is_empty():
            custom_heap.extract_max()
        custom_times.append(time.perf_counter() - t0)

        # Benchmark Python built-in heapq
        built_in_heap = []
        t0 = time.perf_counter()
        for task in test_tasks:
            heapq.heappush(built_in_heap, (-task.priority, task.name))
        while built_in_heap:
            heapq.heappop(built_in_heap)
        builtin_times.append(time.perf_counter() - t0)

    # Plotting results
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, custom_times, 'r-o', label='Custom Max-Heap (Python)')
    plt.plot(sizes, builtin_times, 'b-s', label='Python built-in heapq (C-optimized)')
    plt.title('Task Scheduler Performance: Custom Max-Heap vs Python heapq')
    plt.xlabel('Number of Tasks')
    plt.ylabel('Execution Time (Seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('task_scheduler_benchmark.png')
    plt.show()
    print("Benchmark complete! Saved plot as 'task_scheduler_benchmark.png'")

if __name__ == "__main__":
    run_benchmark_and_plot()