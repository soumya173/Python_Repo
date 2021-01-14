import sys

class MergeSort:
    # def __init__(self, arr):
    #     self._arr = arr
    #     self._len = len(arr)

    def display(self, arr):
        if len(arr) == 0:
            print(f'No elements in array {arr}')
            return
        for el in arr:
            print(el, end=' -> ')
        print("")

    def _merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to the temporary arrays
        for i in range(n1):
            L[i] = arr[left + i]
        for i in range(n2):
            R[i] = arr[mid + i + 1]

        # Merge the elements in sorted order
        i = j =0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Copy the remaining elements if any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1


    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (right + left) // 2
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid+1, right)
            self._merge(arr, left, mid, right)
        # return self._arr

def main():
    arr = [12, 11, 13, 5, 6, 7]
    msort = MergeSort()
    print('Original List:')
    msort.display(arr)
    msort.merge_sort(arr, 0, len(arr)-1)
    print('Sorted List:')
    msort.display(arr)

    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
