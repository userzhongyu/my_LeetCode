from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])

        visit = [[False] * m for _ in range(n)]

        def dfs(_i: int, _j: int):
            # 越界、当前访问元素不为 X 或者已经访问过当前元素，跳出递归
            if _i < 0 or _i + 1 >= len(board) or _j < 0 or _j + 1 >= len(board[0]) or board[_i][_j] == 'X' or visit[_i][
                _j]:
                return
            visit[_i][_j] = True
            # # 左边缘
            # if _j + 1 < len(board[0]) and board[_i][_j + 1] == 'O' and not visit[_i][_j + 1]:
            #     dfs(_i, _j + 1)
            # # 上边缘
            # if _i + 1 < len(board) and board[_i + 1][_j] == 'O' and not visit[_i + 1][_j]:
            #     dfs(_i + 1, _j)
            # # 右边缘
            # if _j > 0 and board[_i][_j - 1] == 'O' and not visit[_i][_j - 1]:
            #     dfs(_i, _j - 1)
            # # 下边缘
            # if _i > 0 and board[_i - 1][_j] == 'O' and not visit[_i - 1][_j]:
            #     dfs(_i - 1, _j)

            # 左边缘
            dfs(_i, _j + 1)
            # 上边缘
            dfs(_i + 1, _j)
            # 右边缘
            dfs(_i, _j - 1)
            # 下边缘
            dfs(_i - 1, _j)

        # 从左右两侧开始延伸
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m - 1] == 'O':
                dfs(i, m - 1)
        # 从上下两侧开始延伸
        for j in range(m):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[n - 1][j] == 'O':
                dfs(n - 1, j)
        # 根据 visit 的值判断能否包围
        for i in range(n):
            for j in range(m):
                if not visit[i][j]:
                    board[i][j] = 'X'


def main():
    # board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    # board = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
    # board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
    # board = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "O"]]
    # board = [["X", "X", "X", "X", "X"], ["X", "O", "O", "O", "X"], ["X", "X", "O", "O", "X"], ["X", "X", "X", "O", "X"], ["X", "O", "X", "X", "X"]]
    board = [["O", "X", "O", "O", "X", "X"], ["O", "X", "X", "X", "O", "X"], ["X", "O", "O", "X", "O", "O"],
             ["X", "O", "X", "X", "X", "X"], ["O", "O", "X", "O", "X", "X"], ["X", "X", "O", "O", "O", "O"]]
    Solution().solve(board)
    print(board)


if __name__ == '__main__':
    main()
