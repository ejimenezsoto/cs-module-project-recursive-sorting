# TO-DO: complete the helper function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    apos = 0
    bpos = 0

    while 1 < 2:
        if bpos >= len(arrB):
            return merged_arr + arrA[apos:]
        if apos >= len(arrA):
            return merged_arr + arrB[bpos:]
        if arrA[apos] < arrB[bpos]:
            merged_arr.append(arrA[apos])
            apos += 1
        else:
            merged_arr.append(arrB[bpos])
            bpos += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = math.floor((0 + len(arr)) // 2)
        left = arr[:mid]
        right = arr[mid:]
        a = merge_sort(left)
        b = merge_sort(right)
        arr = merge(a, b)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
