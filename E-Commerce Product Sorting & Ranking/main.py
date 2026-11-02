import time
import random
import matplotlib.pyplot as plt

# ==========================================
# 1. Insertion Sort Algorithm
# ==========================================
def insertion_sort(arr, key='price', reverse=False):
    a = arr.copy()
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0 and ((a[j][key] < current[key]) if reverse else (a[j][key] > current[key])):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = current
    return a


# ==========================================
# 2. Divide and Conquer: Merge Sort Algorithm
# ==========================================
def merge_sort(arr, key='price', reverse=False):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, reverse)
    right = merge_sort(arr[mid:], key, reverse)
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        condition = (left[i][key] >= right[j][key]) if reverse else (left[i][key] <= right[j][key])
        if condition:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ==========================================
# 3. Quick Sort Algorithm
# ==========================================
def quick_sort(arr, key='price', reverse=False):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2][key]
    
    if reverse:
        left = [x for x in arr if x[key] > pivot]
        middle = [x for x in arr if x[key] == pivot]
        right = [x for x in arr if x[key] < pivot]
    else:
        left = [x for x in arr if x[key] < pivot]
        middle = [x for x in arr if x[key] == pivot]
        right = [x for x in arr if x[key] > pivot]
        
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)


# ==========================================
# Main Execution & Benchmark
# ==========================================
def generate_products(n):
    categories = ['Laptop', 'Phone', 'Headphones', 'Monitor', 'Keyboard']
    products = []
    for i in range(1, n + 1):
        products.append({
            'id': i,
            'name': f"{random.choice(categories)}_{i}",
            'price': round(random.uniform(50.0, 2000.0), 2),
            'rating': round(random.uniform(1.0, 5.0), 1)
        })
    return products

def main():
    print("=" * 60)
    print("      E-COMMERCE PRODUCT SORTING SYSTEM BENCHMARK      ")
    print("=" * 60)
    
    # 1. عرض تجربة مصغرة على 5 منتجات
    sample_products = generate_products(5)
    print("\n--- Original Sample Products ---")
    for p in sample_products:
        print(p)

    sorted_sample = quick_sort(sample_products, key='price', reverse=False)
    print("\n--- Products Sorted by Price (Lowest to Highest via QuickSort) ---")
    for p in sorted_sample:
        print(p)

    # 2. قياس الأداء للكميات الكبيرة من البيانات
    sizes = [100, 500, 1000, 2000, 3000]
    times_insertion = []
    times_merge = []
    times_quick = []

    print("\nBenchmarking performance on larger datasets...")
    for n in sizes:
        dataset = generate_products(n)

        # Insertion Sort Time
        t0 = time.perf_counter()
        insertion_sort(dataset, key='price')
        times_insertion.append(time.perf_counter() - t0)

        # Merge Sort Time (Divide & Conquer)
        t0 = time.perf_counter()
        merge_sort(dataset, key='price')
        times_merge.append(time.perf_counter() - t0)

        # Quick Sort Time
        t0 = time.perf_counter()
        quick_sort(dataset, key='price')
        times_quick.append(time.perf_counter() - t0)

    # 3. رسم المنحنى البياني للأداء
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, times_insertion, 'r-o', label='Insertion Sort O(n^2)')
    plt.plot(sizes, times_merge, 'g-s', label='Merge Sort - Divide & Conquer O(n log n)')
    plt.plot(sizes, times_quick, 'b-^', label='Quick Sort O(n log n)')
    
    plt.title('Sorting Algorithm Performance on E-Commerce Dataset')
    plt.xlabel('Number of Products (n)')
    plt.ylabel('Time (Seconds)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('sorting_benchmark.png')
    plt.show()
    
    print("\nBenchmark finished! Graph saved as 'sorting_benchmark.png'")

if __name__ == '__main__':
    main()