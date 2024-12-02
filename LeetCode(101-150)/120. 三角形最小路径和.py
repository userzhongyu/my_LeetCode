import copy
import math
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1]) + 1
        dp = [[math.inf] * n for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            for j in range(1, n):
                if j - 1 < len(triangle[i - 1]):
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i - 1][j - 1]
        # print(dp)
        return min(dp[-1][:])


def main():
    # triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    triangle = [[-1]]
    print(Solution().minimumTotal(triangle))



if __name__ == '__main__':
    main()
