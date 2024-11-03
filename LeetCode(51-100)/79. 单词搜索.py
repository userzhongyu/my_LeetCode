from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i, j, index):
            # 字符不匹配
            if board[i][j] != word[index]:
               return False
            # 字符完全匹配
            if index == len(word) - 1:
                return True

            # 当前字符串均匹配,修改当前最后的字符
            # 递归越深入,被修改的字符越多
            board[i][j] = '*'
            for path in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i = i + path[0]
                new_j = j + path[1]
                if 0 <= new_i < row and 0 <= new_j < col and dfs(new_i, new_j, index + 1):
                    return True
            # 恢复原字符
            board[i][j] = word[index]

        # 寻找入口
        for p in range(row):
            for q in range(col):
                if dfs(p, q, 0):
                    return True

        return False


def main():
    board = eval(input())
    word = eval(input())
    print(Solution().exist(board, word))


if __name__ == '__main__':
    main()
