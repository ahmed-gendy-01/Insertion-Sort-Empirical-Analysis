import time
import random
import sys
import matplotlib.pyplot as plt

# رفع حد التكرار لمنع حدوث خطأ أثناء تنفيذ Quick Sort
sys.setrecursionlimit(30000)

# 1. Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# 2. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 3. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 4. Benchmark Function
def measure_time(sort_func, arr):
    t0 = time.perf_counter()
    sort_func(arr)
    return time.perf_counter() - t0

def run_benchmark():
    sizes = [100, 500, 1000, 2000, 3000, 5000]
    
    algorithms = {
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort,
        'Python sorted()': sorted
    }
    
    scenarios = ['Random', 'Sorted', 'Reverse-Sorted']
    
    results = {scenario: {alg: [] for alg in algorithms} for scenario in scenarios}

    for n in sizes:
        # تجهيز المصفوفات
        data_random = [random.randint(1, 100000) for _ in range(n)]
        data_sorted = list(range(n))
        data_reverse = list(range(n, 0, -1))
        
        datasets = {
            'Random': data_random,
            'Sorted': data_sorted,
            'Reverse-Sorted': data_reverse
        }
        
        for scenario_name, data in datasets.items():
            for alg_name, alg_func in algorithms.items():
                # تجاوز Insertion Sort في الأعداد الكبيرة جداً لتفادي البطء الشديد
                if alg_name == 'Insertion Sort' and n > 3000 and scenario_name != 'Sorted':
                    results[scenario_name][alg_name].append(None)
                    continue
                t = measure_time(alg_func, data)
                results[scenario_name][alg_name].append(t)

    # رسم النتائج في 3 مخططات بيانية
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    for idx, scenario_name in enumerate(scenarios):
        ax = axes[idx]
        for alg_name in algorithms:
            times = results[scenario_name][alg_name]
            valid_sizes = [sizes[i] for i in range(len(times)) if times[i] is not None]
            valid_times = [t for t in times if t is not None]
            ax.plot(valid_sizes, valid_times, marker='o', label=alg_name)
            
        ax.set_title(f'Performance: {scenario_name} Input')
        ax.set_xlabel('Array Size (n)')
        ax.set_ylabel('Time (Seconds)')
        ax.legend()
        ax.grid(True)
        
    plt.tight_layout()
    plt.savefig('sorting_benchmark_results.png')
    plt.show()

if __name__ == '__main__':
    run_benchmark()