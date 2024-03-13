"""
只考虑列号,全排列
检查斜边: 左上->行号与列号的差相同,右上->行号与列号的和相同
排列出来的组合当做位置放入'Q',剩余位置放入'.'
https://leetcode.cn/problems/n-queens/solutions/2079586/hui-su-tao-lu-miao-sha-nhuang-hou-shi-pi-mljv/
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n  # 皇后位置在每一行的列号
        on_path = [False] * n  # 标记备选元素

        def dfs(row):
            if row == n:
                res.append(['.' * col + 'Q' + '.' * (n - col - 1) for col in path])
                return
            for col, on in enumerate(on_path):
                # 从备选元素中找到攻击不了左上、右上的位置
                # chess[row][col]左上的棋子[i][j]满足i - j == row - col,右上的棋子[i][j]满足i + j == row + col
                if not on and all(row + col != R + path[R] and row - col != R - path[R] for R in range(row)):
                    path[row] = col
                    on_path[col] = True
                    dfs(row + 1)
                    # 恢复现场
                    path[row] = 0
                    on_path[col] = False

        dfs(0)
        return res



def main():
    n = eval(input())
    print(Solution().solveNQueens(n))


if __name__ == '__main__':
    main()