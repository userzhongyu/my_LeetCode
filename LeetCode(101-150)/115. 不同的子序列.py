from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        lens = len(s)
        lent = len(t)

        dp = [[0] * (lent + 1) for _ in range(lens + 1)]

        # 遍历 dp 数组
        for i in range(1, lens + 1):
            for j in range(1, lent + 1):
                if s[i - 1] == t[j - 1]:
                    if j == 1:
                        dp[i][j] = dp[i - 1][j] + 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


def main():
    s = "babgbag"
    t = "bag"
    # s = "rabbbit"
    # t = "rabbit"
    # s = "a"
    # t = "b"
    print(Solution().numDistinct(s, t))


if __name__ == '__main__':
    main()
