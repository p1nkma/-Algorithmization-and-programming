"""
Написать декоратор, который будет вычислять время работы сортировки.
2.  Шейкерная сортировка (Shaker sort)
3.  Сортировка расчёской (Comb sort)
4.  Сортировка слиянием (Merge Sort)
5.  Быстрая сортировка или сортировка Хоара (Quick Sort)
6.  Сортировка вставками / Insertion sort
7.  Сортировка Шелла / Shellsort
8.  Сортировка деревом / Tree sort
10. Сортировка выбором / Selection sort
11. Пирамидальная сортировка / Heapsort
12. Сортировка подсчетом / Counting sort
13. Блочная сортировка / Bucket sort
14. Поразрядная сортировка / Radix sort
15. Битонная сортировка, Битоническая сортировка / Bitonic sort
16. Timsort
"""

import functools
import random
import time
import unittest


# 1. Декоратор: замер времени выполнения
def measure_execution_time(func):
    @functools.wraps(func)
    def timed_execution(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"Function {func.__name__} took {duration:.8f} seconds to execute")
        return result
    return timed_execution


# 2. Шейкерная сортировка  O(n^2)
@measure_execution_time
def shaker_sort(arr):
    a = arr[:]
    left, right = 0, len(a) - 1
    while left < right:
        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1
        for i in range(right, left, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
        left += 1
    return a


# 3. Сортировка расчёской  O(n^2)
@measure_execution_time
def comb_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n
    factor = 1.247
    is_sorted = False
    while not is_sorted:
        gap = int(gap / factor)
        if gap <= 1:
            gap = 1
            is_sorted = True
        for i in range(n - gap):
            if a[i] > a[i + gap]:
                a[i], a[i + gap] = a[i + gap], a[i]
                is_sorted = False
    return a


# 4. Сортировка слиянием  O(n*log n)
def merge(left, right):
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def merge_rec(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(merge_rec(a[:mid]), merge_rec(a[mid:]))

@measure_execution_time
def merge_sort(arr):
    return merge_rec(arr[:])


# 5. Быстрая сортировка (Хоара)  O(n*log n)
def quick_rec(a, low, high):
    if low < high:
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        pi = i + 1
        quick_rec(a, low, pi - 1)
        quick_rec(a, pi + 1, high)

@measure_execution_time
def quick_sort(arr):
    a = arr[:]
    quick_rec(a, 0, len(a) - 1)
    return a


# 6. Сортировка вставками  O(n^2)
@measure_execution_time
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# 7. Сортировка Шелла  O(n^2) в худшем случае
@measure_execution_time
def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


# 8. Сортировка деревом O(n*log n)
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def bst_insert(root, val):
    if root is None:
        return BSTNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    else:
        root.right = bst_insert(root.right, val)
    return root

def inorder(root, res):
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)

@measure_execution_time
def tree_sort(arr):
    root = None
    for x in arr:
        root = bst_insert(root, x)
    res = []
    inorder(root, res)
    return res


# 10. Сортировка выбором  O(n^2)
@measure_execution_time
def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# 11. Пирамидальная сортировка  O(n*log n)
def heapify(a, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

@measure_execution_time
def heap_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a


# 12. Сортировка подсчётом  O(n)
@measure_execution_time
def counting_sort(arr):
    if not arr:
        return []
    min_val, max_val = min(arr), max(arr)
    count = [0] * (max_val - min_val + 1)
    for x in arr:
        count[x - min_val] += 1
    res = []
    for i, c in enumerate(count):
        res.extend([i + min_val] * c)
    return res


# 13. Блочная сортировка  O(n) в среднем
@measure_execution_time
def bucket_sort(arr):
    if not arr:
        return []
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return arr[:]
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for x in arr:
        idx = int((x - min_val) / (max_val - min_val + 1) * n)
        idx = min(idx, n - 1)
        buckets[idx].append(x)
    res = []
    for bucket in buckets:
        bucket.sort()
        res.extend(bucket)
    return res


# 14. Поразрядная сортировка  O(n*k)
def counting_pass(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for x in arr:
        count[(x // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
    return output

@measure_execution_time
def radix_sort(arr):
    a = arr[:]
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        a = counting_pass(a, exp)
        exp *= 10
    return a


# 15. Битонная сортировка  O(n*log^2 n)
def bitonic_compare(a, i, j, ascending):
    if (a[i] > a[j]) == ascending:
        a[i], a[j] = a[j], a[i]

def bitonic_merge(a, low, count, ascending):
    if count > 1:
        k = count // 2
        for i in range(low, low + k):
            bitonic_compare(a, i, i + k, ascending)
        bitonic_merge(a, low, k, ascending)
        bitonic_merge(a, low + k, k, ascending)

def bitonic_rec(a, low, count, ascending):
    if count > 1:
        k = count // 2
        bitonic_rec(a, low, k, True)
        bitonic_rec(a, low + k, k, False)
        bitonic_merge(a, low, count, ascending)

@measure_execution_time
def bitonic_sort(arr):
    # Дополняем до степени двойки
    n = len(arr)
    p = 1
    while p < n:
        p <<= 1
    a = arr[:] + [float('inf')] * (p - n)
    bitonic_rec(a, 0, p, True)
    return [x for x in a if x != float('inf')]


# 16. Timsort  O(n*log n)  — встроенный алгоритм Python
@measure_execution_time
def timsort(arr):
    return sorted(arr)


# Тесты
class TestSortAlgorithms(unittest.TestCase):

    def setUp(self):
        random.seed(42)
        self.test_arr = [random.randint(0, 1000) for _ in range(100)]
        self.expected_result = sorted(self.test_arr)
        self.algos = [
            shaker_sort, comb_sort, merge_sort, quick_sort,
            insertion_sort, shell_sort, tree_sort, selection_sort,
            heap_sort, counting_sort, bucket_sort, radix_sort,
            bitonic_sort, timsort
        ]

    def test_correctness(self):
        for algo in self.algos:
            with self.subTest(algo=algo.__name__):
                res = algo(self.test_arr)
                self.assertEqual(res, self.expected_result)

    def test_growing_array(self):
        print("\n--- ТЕСТ: РОСТ МАССИВА ---")
        for length in [100, 500, 1000]:
            print(f"\nДлина массива: {length}")
            test_arr = [random.randint(0, 10000) for _ in range(length)]
            for algo in self.algos:
                algo(test_arr)


if __name__ == '__main__':
    unittest.main()
