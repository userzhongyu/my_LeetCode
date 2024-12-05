import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-math.inf] * 3 for _ in range(2)] for _ in range(n)]

        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]

        for i in range(1, n):
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][1][0])
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][1][0] + prices[i])
            dp[i][0][2] = max(dp[i - 1][0][2], dp[i - 1][1][1] + prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], -prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][1] - prices[i])
            dp[i][1][2] = max(dp[i - 1][1][2], dp[i - 1][0][2] - prices[i])

        return max(dp[-1][0])  # 只考虑最后未持有的状态，持有的时候收益一定比未持有的低


def main():
    # prices = [1, 2, 3, 4, 5]
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [2, 1, 2, 0, 1]
    print(Solution().maxProfit(prices))


if __name__ == '__main__':
    main()
