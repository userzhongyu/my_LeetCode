class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # 在word1,word2前"插入"一个字符,用于处理word1或word2为空的情况
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(n + 1):
            dp[i][0] = i

        # 状态转移
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i - 1][j - 1]表示word1需要替换一个字符
                    # dp[i][j - 1]表示word1需要插入一个字符
                    # dp[i - 1][j]表示word1需要删除一个字符
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[n][m]


def main():
    word1 = eval(input())
    word2 = eval(input())
    print(Solution().minDistance(word1, word2))


if __name__ == '__main__':
    main()