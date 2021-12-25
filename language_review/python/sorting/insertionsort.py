from typing import List


def insertionSort(arr: List[int]):
    '''
    Insertion sort is an inplace stable sorting algo

    Time Complexity:
        O(n^2) quadratic time worst case
        O(n^2) quadratic time average case
        O(n) linear time      best case

    Space Complexity:   
        O(1) constant space 
    '''
    N = len(arr)
    for i in range(1, N):
        j = i
        # Check for values to the left that are smaller and swap if needed
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1


def printList(values):
    for val in values:
        print(val, end=" ")
    print()


def driver():
    values = [5, 4, 3, 2, 1, 2, 3, 4, 7, 8, 8, 6]
    print("List before insertion sort:")
    printList(values)
    insertionSort(values)
    print("List after insertion sort:")
    printList(values)


if __name__ == "__main__":
    driver()
