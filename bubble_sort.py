# bubble sort
# Time complexity: O(n^2)
# Space complexity: O(1)

def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1] and not reverse) or (arr[j] < arr[j+1] and reverse):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
