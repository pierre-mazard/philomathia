# merge sort
# Time complexity: O(n log n)
# Space complexity: O(n)

def merge_sort(arr, reverse=False):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, reverse)
        merge_sort(R, reverse)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if (L[i] < R[j] and not reverse) or (L[i] > R[j] and reverse):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
