import time
import random
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key
        shifts += 1
        
    return comparisons, shifts

def run_experiment():
    sizes = list(range(100, 5001, 300))
    
    times_sorted, times_reverse, times_random = [], [], []

    for n in sizes:
        # 1. Sorted Input
        arr_sorted = list(range(n))
        t0 = time.perf_counter()
        insertion_sort(arr_sorted)
        t1 = time.perf_counter()
        times_sorted.append(t1 - t0)

        # 2. Reverse-Sorted Input
        arr_rev = list(range(n, 0, -1))
        t0 = time.perf_counter()
        insertion_sort(arr_rev)
        t1 = time.perf_counter()
        times_reverse.append(t1 - t0)

        # 3. Random Input
        arr_rand = [random.randint(1, 100000) for _ in range(n)]
        t0 = time.perf_counter()
        insertion_sort(arr_rand)
        t1 = time.perf_counter()
        times_random.append(t1 - t0)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_sorted, 'g-o', label='Empirical: Sorted (Best Case)')
    plt.plot(sizes, times_random, 'b-s', label='Empirical: Random (Average Case)')
    plt.plot(sizes, times_reverse, 'r-^', label='Empirical: Reverse (Worst Case)')
    
    n_arr = np.array(sizes)
    c_linear = times_sorted[-1] / n_arr[-1]
    c_quad = times_reverse[-1] / (n_arr[-1] ** 2)
    
    plt.plot(n_arr, c_linear * n_arr, 'g--', label=r'Theoretical $O(n)$')
    plt.plot(n_arr, c_quad * (n_arr ** 2), 'r--', label=r'Theoretical $O(n^2)$')
    
    plt.title('Insertion Sort: Running Time vs. Array Size (n)')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (Seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('insertion_sort_analysis.png')
    plt.show()

if __name__ == "__main__":
    run_experiment()