''' 
Common Problem Description:
Move all Zeros (target) to the left (or right) of an array inplace 
while maintaining ordering of non-target values.

Example Input:
arr = [1, 10, 20, 0, 58, 63, 0, 88, 0]
target = 0

Expected Output:
[0, 0, 0, 1, 10, 20, 58, 63, 88]
'''


def swap(arr, swapA, swapB):
    arr[swapA], arr[swapB] = arr[swapB], arr[swapA]


def move_target_to_right(arr, target):
    N = len(arr)
    reserved = 0
    for i in range(N):
        if arr[i] == target:
            reserved += 1
        elif reserved > 0:
            swap(arr, i, i - reserved)


def move_target_to_left(arr, target):
    N = len(arr)
    reserved = 0
    for i in reversed(range(N)):
        if arr[i] == target:
            reserved += 1
        elif reserved > 0:
            swap(arr, i, i + reserved)


def main():
    zeroes_moved_right = [1, 10, 20, 0, 58, 63, 0, 88, 0]
    move_target_to_right(zeroes_moved_right, 0)
    assert zeroes_moved_right == [1, 10, 20, 58, 63, 88, 0, 0, 0]

    nines_moved_left = [1, 10, 20, 9, 58, 63, 9, 88, 9]
    move_target_to_left(nines_moved_left, 9)
    assert nines_moved_left == [9, 9, 9, 1, 10, 20, 58, 63, 88]


if __name__ == '__main__':
    main()
