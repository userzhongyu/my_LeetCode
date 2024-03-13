"""
动态规划
(i,j)处的路径总数为(i - 1, j) + (i, j - 1)
初始化: (0, *) (*, 0)全为1 只有一种到达路径
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


def main():
    m = int(input())
    n = int(input())
    print(Solution().uniquePaths(m, n))


if __name__ == '__main__':
    main()



