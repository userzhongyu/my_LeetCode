class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = [0]
        col = [0] * n  # 列号
        on_path = [False] * n
        # 用来记录斜上方向是否放有皇后
        le_up = [False] * 2 * n
        ri_up = [False] * 2 * n

        def dfs(row):
            if row == n:
                ans[0] += 1
                return

            for c, on in enumerate(on_path):
                if not on and not le_up[row - c] and not ri_up[row + c]:
                    col[row] = c
                    on_path[c] = le_up[row - c] = ri_up[row + c] = True
                    dfs(row + 1)
                    on_path[c] = le_up[row - c] = ri_up[row + c] = False
                    col[row] = 0

        dfs(0)
        return ans[0]


def main():
    n = eval(input())
    print(Solution().totalNQueens(n))


if __name__ == '__main__':
    main()