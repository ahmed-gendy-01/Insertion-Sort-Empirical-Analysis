# E-Commerce Product Sorting & Ranking Analysis

This project simulates an e-commerce catalog sorting engine using three core algorithms learned in the **Analysis of Algorithms** course:

1. **Insertion Sort** ($O(n^2)$)
2. **Merge Sort** (Divide and Conquer Approach, $O(n \log n)$)
3. **Quick Sort** ($O(n \log n)$ average)

## Features
- Sorts product datasets by `price` or `rating`.
- Compares real execution times across varying dataset sizes (100 to 3,000 items).
- Generates a performance chart saved as `sorting_benchmark.png`.

## Execution
```bash
pip install matplotlib
python main.py