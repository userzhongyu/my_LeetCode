from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 初始化dp数组
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
            # 只要出现障碍物,下方全部无法到达
                break
            else:
                dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
            # 只要出现障碍物,下方全部无法到达
                break
            else:
                dp[0][i] = 1

        # 计算dp[i][j]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


def main():
    obstacleGrid = eval(input())
    print(Solution().uniquePathsWithObstacles(obstacleGrid))


if __name__ == '__main__':
    main()


