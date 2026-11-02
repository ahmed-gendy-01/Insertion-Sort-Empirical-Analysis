# Sorting Benchmark Lab

An empirical benchmark laboratory comparing four sorting algorithms in Python across different input distributions and array sizes.

## Algorithms Evaluated
1. **Insertion Sort** ($O(n^2)$ worst-case)
2. **Merge Sort** ($O(n \log n)$)
3. **Quick Sort** ($O(n \log n)$ average-case)
4. **Python Built-in `sorted()`** (Timsort, $O(n \log n)$)

## Benchmark Scenarios
- **Random Data:** Unordered integer arrays.
- **Sorted Data:** Best-case scenario for adaptive algorithms.
- **Reverse-Sorted Data:** Worst-case scenario for basic quadratic algorithms.

## Execution
```bash
pip install matplotlib
python main.py