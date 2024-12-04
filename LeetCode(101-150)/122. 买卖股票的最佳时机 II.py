from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n)]

        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], prices[i] + dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]



def main():
    prices = [7, 1, 5, 3, 6, 4]
    # prices =[1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))


if __name__ == '__main__':
    main()


