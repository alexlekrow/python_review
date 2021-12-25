''' 
Common Problem Description:
clear


Example Input:
[1, 10, 20, 0, 58, 63, 0, 88, 0]

Expected Output:
[0, 0, 0, 1, 10, 20, 58, 63, 88]
'''


def move_target_to_right(A, target):
    reserved = 0
    for i in range(len(A)):
        if A[i] == target:
            reserved += 1
        elif reserved > 0:
            A[i], A[i - reserved] = A[i - reserved], A[i]


def move_target_to_left(A, target):
    reserved = 0
    for i in reversed(range(len(A))):
        if A[i] == target:
            reserved += 1
        elif reserved > 0:
            A[i], A[i + reserved] = A[i + reserved], A[i]


def driver():
    A = [1, 10, 20, 0, 58, 63, 0, 88, 0]
    move_target_to_right(A, 0)
    print(A)


if __name__ == '__main__':
    driver()
