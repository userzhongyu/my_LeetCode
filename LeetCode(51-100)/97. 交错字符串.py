class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        s1 = '*' + s1
        s2 = '*' + s2
        dp = [[False] * len(s2) for _ in range(len(s1))]
        dp[0][0] = True
        print(dp)
        for i in range(len(s1)):
            for j in range(len(s2)):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i] == s3[i + j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] and s1[i] == s3[i + j - 1] or dp[i][j - 1] and s2[j] == s3[i + j - 1]
        return dp[-1][-1]




def main():
    # s1 = "aabcc"
    # s2 = "dbbca"
    # s3 = "aadbbcbcac"
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    # s1 = 'a'
    # s2 = ''
    # s3 = 'a'
    print(Solution().isInterleave(s1, s2, s3))


if __name__ == '__main__':
    main()
