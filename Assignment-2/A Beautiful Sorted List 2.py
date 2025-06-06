def partition(arr3, start, end):
    pivot = arr3[end]
    left = start
    right = end - 1
    while left <= right:
        while left <= right and arr3[left] < pivot:
            left += 1
        while left <= right and arr3[right] > pivot:
            right -= 1

        if left <= right:
            arr3[left], arr3[right] = arr3[right], arr3[left]
            left += 1
            right -= 1
    arr3[left], arr3[end] = arr3[end], arr3[left]
    return left
def quicksrt(arr3, start, end):
    if start >= end:
        return
    middle = partition(arr3, start, end)
    quicksrt(arr3, start, middle - 1)
    quicksrt(arr3, middle + 1, end)
n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))
arr3 = arr1 + arr2
quicksrt(arr3, 0, len(arr3) - 1)
print(*arr3)
