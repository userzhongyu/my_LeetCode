from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        start = [['.'] * n for _ in range(n)]   # 初始化棋盘

        def dfs(path: List[List[str]], count: int, new_i: int, new_j: int):
            for index in range(n):
                # 检查行
                if path[new_i][index] == 'Q':
                    if index != new_j:
                        return
                # 检查列
                if path[index][new_j] == 'Q':
                    if index != new_i:
                        return

            # 检查斜边
            # 左上、右上
            left_j = new_j - 1
            right_j = new_j + 1
            for i in range(new_i - 1, -1, -1):
                if left_j >= 0:
                    if path[i][left_j] == 'Q':
                        return
                    else:
                        left_j -= 1
                if right_j < n:
                    if path[i][right_j] == 'Q':
                        return
                    else:
                        right_j += 1
            # # 从上往下放置皇后,所以不用考虑下方的行
            # # 左下、右下
            # left_j = new_j - 1
            # right_j = new_j + 1
            # for i in range(new_i + 1, n):
            #     if left_j >= 0:
            #         if path[i][left_j] == 'Q':
            #             return
            #         else:
            #             left_j -= 1
            #     if right_j < n:
            #         if path[i][right_j] == 'Q':
            #             return
            #         else:
            #             right_j += 1

            # 在当前位置摆放皇后,不与之前状态发送冲突
            # 检查皇后数量
            if count == n:
                temp = []
                for i in range(n):
                    temp.append(''.join(path[i]))
                res.append(temp[:])
                return
            # 深入
            for i in range(new_i + 1, n):
                for j in range(n):
                    if j == new_j:
                        continue
                    path[i][j] = 'Q'
                    count += 1
                    dfs(path, count, i, j)
                    path[i][j] = '.'
                    count -= 1

        dfs(start, 0, -1, -1)
        return res


def main():
    n = eval(input())
    print(Solution().solveNQueens(n))


if __name__ == '__main__':
    main()