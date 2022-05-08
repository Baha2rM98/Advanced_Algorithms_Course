def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end


def quick_sort(start, end, arr):
    if start < end:
        p = partition(start, end, arr)
        quick_sort(start, p - 1, arr)
        quick_sort(p + 1, end, arr)


def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


my_list = [5, 12, 11, 13, -1, 89, 5, 6, 7]
print("Given array is", end="\n")
print_list(my_list)
quick_sort(0, len(my_list) - 1, my_list)
print("Sorted array is: ", end="\n")
print_list(my_list)
