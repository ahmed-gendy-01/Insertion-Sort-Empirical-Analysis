# OS Task Scheduler Simulation (Max-Heap)

A Python implementation of an Operating System Task Scheduler using a **Max-Heap** data structure built from scratch, as part of the *Analysis of Algorithms* course mini-projects.

## Features & Milestones
1. **Task Model:** Encapsulates task attributes including `name`, `priority`, and `arrival_time`.
2. **Custom Max-Heap:** Implemented `INSERT` ($O(\log n)$) and `EXTRACT-MAX` ($O(\log n)$) methods without using external libraries.
3. **Task Execution Simulation:** Simulates prioritization and execution of 10 dynamic tasks.
4. **Performance Benchmark:** Compares custom implementation runtime against Python's built-in `heapq` module for 100,000 tasks.

## Requirements & Execution
- **Python 3.x**

Run the project directly via terminal:
```bash
python main.py