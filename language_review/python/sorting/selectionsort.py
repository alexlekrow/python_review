from typing import List


def selectionSort(arr: List[int]):
    '''
    * Selection sort is an inplace unstable sorting algo

    Time Complexity:
        Best    -   O(n^2) 
        Average -   O(n^2)
        Worst   -   O(n^2)

    Space Complexity 
                -   O(1)
    '''
    N = len(arr)
    for i in range(N):
        minIndex = i
        for j in range(i, N):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # swap location of values if needed
        if minIndex > i:
            arr[minIndex], arr[i] = arr[i], arr[minIndex]


def printList(values):
    for val in values:
        print(val, end=" ")
    print()


def driver():
    values = [5, 4, 3, 2, 1, 2, 3, 4, 7, 8, 8, 6]
    print("List before selection sort:")
    printList(values)
    selectionSort(values)
    print("List after selection sort:")
    printList(values)


if __name__ == "__main__":
    driver()
