def merge_sort(arr):
    if len(arr) > 1:
        middle = int(len(arr) / 2)
        left_side = arr[:middle]
        right_side = arr[middle:]
        merge_sort(left_side)
        merge_sort(right_side)
        i = j = k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                arr[k] = left_side[i]
                i += 1
            else:
                arr[k] = right_side[j]
                j += 1
            k += 1
        while i < len(left_side):
            arr[k] = left_side[i]
            i += 1
            k += 1
        while j < len(right_side):
            arr[k] = right_side[j]
            j += 1
            k += 1


def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


my_list = [5, 12, 11, 13, -1, 89, 5, 6, 7]
print("Given array is", end="\n")
print_list(my_list)
merge_sort(my_list)
print("Sorted array is: ", end="\n")
print_list(my_list)
