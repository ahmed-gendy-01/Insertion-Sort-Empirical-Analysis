# Empirical Analysis of Insertion Sort

This repository presents an empirical runtime and operation-count analysis of **Insertion Sort** across Sorted, Reverse-sorted, and Random input sets, with a detailed comparison against **Merge Sort**.

## Project Files
- `main.py`: Python script for timing, counting operations, and plotting graphs.
- `insertion_sort_analysis.png`: Chart comparing empirical runtimes against theoretical bounds.

## Comparison: Insertion Sort vs. Merge Sort

| Property | Insertion Sort | Merge Sort |
| :--- | :--- | :--- |
| **Best Case** | $O(n)$ | $O(n \log n)$ |
| **Average Case** | $O(n^2)$ | $O(n \log n)$ |
| **Worst Case** | $O(n^2)$ | $O(n \log n)$ |
| **Auxiliary Space** | $O(1)$ | $O(n)$ |
| **Adaptability** | Yes (Fast on sorted data) | No |