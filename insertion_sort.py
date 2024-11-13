# insertion sort 
# Time complexity: O(n^2)
# Space complexity: O(1)

def insertion_sort(arr, reverse=False):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and ((key < arr[j] and not reverse) or (key > arr[j] and reverse)):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
