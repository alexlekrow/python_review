import sys
import re
import copy
import pprint as pp
from pathlib import Path
from typing import List


def invertRowsInPlace(matrix: List[List[int]]):
    N = len(matrix)
    for row in matrix:
        for i in range(N // 2):
            row[i], row[N - 1 - i] = row[N - 1 - i], row[i]


def invertColumnsInPlace(matrix: List[List[int]]):
    N = len(matrix)
    for topRow in range(N // 2):
        bottomRow = N - 1 - topRow
        for col in range(N):
            matrix[topRow][col], matrix[bottomRow][col] = matrix[bottomRow][col], matrix[topRow][col]


def transposeInPlace(matrix: List[List[int]]):
    for i in range(len(matrix)):
        for j in range(i):  # we can ignore all values on, or past the diagonal (j == i) or (j > i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotateArray(matrix: List[List[int]]):
    # invertRowsInPlace(matrix)
    # Column invert + transpose == clockwise rotation
    # Row invert + transpose == counter-clockwise rotation
    invertColumnsInPlace(matrix)
    transposeInPlace(matrix)

    for row in matrix:
        print(row)


def rotate2DArrayClockwise(A):
    startOffset = 0
    limit = len(A) // 2
    # print(f"limit: {limit}")

    while startOffset < limit:
        # print(f"offset: {startOffset}")
        endOffset = len(A) - startOffset
        endIndex = endOffset - 1

        top = A[startOffset][startOffset:endOffset]
        bottom = A[endIndex][startOffset:endOffset]
        left = []
        right = []

        copyFrom = 0
        for row in A[startOffset:endOffset]:
            # Save left columns values for use later
            left.append(row[startOffset])
            # Write the saved values from bottom row to our left column
            row[startOffset] = bottom[copyFrom]
            # Save right columns values for use later
            right.append(row[endIndex])
            # Write the saved values from top row to our right column
            row[endIndex] = top[copyFrom]
            copyFrom += 1

        # Write the saved values from left column (in reversed order) to our top row
        A[startOffset][startOffset:endOffset] = reversed(left)
        # Write the saved values from right column (in reversed order) to our bottom row
        A[endIndex][startOffset:endOffset] = reversed(right)
        startOffset += 1


def driver():
    values = ['a', 'b', 'c', 'zyeah']
    for val in values:
        print(val)


if __name__ == "__main__":
    driver()
