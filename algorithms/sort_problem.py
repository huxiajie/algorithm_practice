# encoding: utf-8
import random


# 选择排序
def selection_sort(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr


# 冒泡排序
def bubble_sort2(arr):
    end = len(arr) - 1
    for i in range(0, len(arr) - 1):
        for j in range(0, end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                end = j
                flag = True
        if not flag:
            break
    return


def bubble_sort1(arr):
    for i in range(0, len(arr) - 1):
        flag = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j] = arr[j], arr[i]
        return arr


# 插入排序
def insertion_sort1(arr):
    for i in range(1, len(arr)):
        index = binary_search(arr, i)
        x = arr[i]
        j = i
        while index != j:
            arr[j] = arr[j - 1]
            j -= 1
        arr[index] = x
    return arr


def binary_search(arr, index):
    x = arr[index]
    begin, end = 0, index - 1
    while begin <= end:
        middle = (begin + end) // 2
        if arr[middle] > x:
            end = middle - 1
        else:
            begin = middle + 1
    return begin


def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j > -1 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    # 不能用for：在i=0时，如果进行了让位置;我们期待j=-1,但是但是用for循环无法达到这个效果
    # 逆序遍历(-1, i-1]
    # for j in range(i - 1, -1, -1):
    #     if item < arr[j]:
    #         arr[j + 1] = arr[j]
    #         j -= 1
    #     else:
    #         break


# 归并排序
def merge_sort(arr, left, right):
    if left >= right:
        return

    middle = (left + right) // 2
    merge_sort(arr, left, middle)
    merge_sort(arr, middle + 1, right)
    arr_tmp = []

    i, j = left, middle + 1
    while i <= middle and j <= right:
        if arr[i] <= arr[j]:
            arr_tmp.append(arr[i])
            i += 1
        else:
            arr_tmp.append(arr[j])
            j += 1
    while i <= middle:
        arr_tmp.append(arr[i])
        i += 1
    while j <= right:
        arr_tmp.append(arr[j])
        j += 1
    for i in range(len(arr_tmp)):
        arr[i] = arr_tmp[i]


# 快速排序
def quick_sort(arr, left, right):
    pass


def quick_sort(arr, left, right):
    if left >= right:
        return

    i, j = left - 1, right + 1
    pivot = arr[(left + right) // 2]
    # pivot_index = random.randint(left, right + 1)
    # pivot = arr[pivot_index]
    while i < j:
        i += 1
        j -= 1
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, left, j)
    quick_sort(arr, j + 1, right)


# 桶排序
def bucket_sort(arr):
    pass


arr = [3, 44, 38, 5, 47, 15, 26, 27, 25, 2, 46, 4, 19, 50, 18, 44]
arr = [3, 44, 38, 5, 46, 4, 19, 50, 18, 44]
arr = [0, 1, 8, 9, 3, 4, 6, 28, 29, 210, 211, 212, 213]
arr = [ 28, 29, 210, 211, 212, 213,0, 1, 8, 9, 3, 4, 6]
arr = [25, 1, 8, 9, 3, 4, 25, 28, 29, 210, 211, 212, 25]
arr = [25, 25, 8, 9, 25, 4, 25, 28, 29, 25, 211, 212, 25]
# arr = [1, 2, 4, 4, 4]
# bubble_sort2(arr)
# selection_sort(arr)
# insertion_sort1(arr)
# merge_sort(arr, 0, len(arr) - 1)
# print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
