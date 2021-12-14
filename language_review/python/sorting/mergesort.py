def mergeSort(arr):
    N = len(arr)
    if N > 1:
        mid = N // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        # Sort subarrays
        mergeSort(leftArr)
        mergeSort(rightArr)

        # Combine subarrays
        l = r = s = 0
        while l < len(leftArr) and r < len(rightArr):
            if leftArr[l] < rightArr[r]:
                arr[s] = leftArr[l]
                l += 1
            else:
                arr[s] = rightArr[r]
                r += 1
            s += 1

        # Copy whatever is remaining from leftArr
        while l < len(leftArr):
            arr[s] = leftArr[l]
            l += 1
            s += 1

        # Copy whatever is remaining from rightArr
        while r < len(rightArr):
            arr[s] = rightArr[r]
            r += 1
            s += 1


def printList(values):
    for val in values:
        print(val, end=" ")
    print()


def driver():
    values = [5, 4, 3, 2, 1, 2, 3, 4, 7, 8, 8, 6]
    printList(values)
    mergeSort(values)
    printList(values)


if __name__ == "__main__":
    driver()
