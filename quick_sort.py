# quick sort
# Time complexity: O(n log n)
# Space complexity: O(log n)

def quick_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if (x <= pivot and not reverse) or (x >= pivot and reverse)]
        greater = [x for x in arr[1:] if (x > pivot and not reverse) or (x < pivot and reverse)]
        return quick_sort(less, reverse) + [pivot] + quick_sort(greater, reverse)
