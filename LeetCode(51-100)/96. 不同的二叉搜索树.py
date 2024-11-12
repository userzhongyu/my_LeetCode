class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[-1]


def main():
    n = 19
    print(Solution().numTrees(n))


if __name__ == '__main__':
    main()
