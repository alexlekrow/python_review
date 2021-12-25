from typing import List


def bubbleSort(arr: List[int]):
    '''
    Bubble sort is an inplace stable sorting algo

    Time Complexity:
        O(n^2) quadratic time worst case
        O(n^2) quadratic time average case
        O(n) linear time      best case

    Space Complexity:   
        O(1) constant space 
    '''
    N = len(arr)
    for i in range(N):
        swapOccurred = False
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapOccurred = True

        if not swapOccurred:
            break


def printList(values):
    for val in values:
        print(val, end=" ")
    print()


def driver():
    values = [5, 4, 3, 2, 1, 2, 3, 4, 7, 8, 8, 6]
    print("List before bubble sort:")
    printList(values)
    bubbleSort(values)
    print("List after bubble sort:")
    printList(values)


if __name__ == "__main__":
    driver()
