"""
先沿水平翻转
再沿对角线翻转
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        # 沿水平翻转
        for i in range(n // 2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - i][j]
                matrix[n - 1 - i][j] = temp
        # 沿对角线翻转
        for i in range(n):
            for j in range(i + 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


def main():
    matrix = eval(input())
    Solution().rotate(matrix)
    print(matrix)


if __name__ == '__main__':
    main()