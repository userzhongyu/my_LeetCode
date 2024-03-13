from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 正无穷
        a = float('inf')
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # 特殊值标记
                    # 改变列
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = a
                    # 改变行
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = a

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == a:
                    matrix[i][j] = 0


def main():
    matrix = eval(input())
    Solution().setZeroes(matrix)
    print(matrix)


if __name__ == '__main__':
    main()