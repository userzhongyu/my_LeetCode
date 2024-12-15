class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # 判断 s[l~r] 左闭右闭，是否为回文
        for r in range(n):
            for l in range(r, -1, -1):
                # s[l~r] 只包含一个字符
                if l == r:
                    dp[l][r] = True
                # s[l~r] 不止包含一个字符，在s[l] == s[r] 的前提下，
                # 1. s[l~r] 只包含2个字符
                # 2. s[l~r] 不止只包含2个字符，根据 s[l+1~r-1] 来判断 s[l~r] 是否为回文
                elif s[l] == s[r]:
                    if r - l == 1 or dp[l + 1][r - 1]:
                        dp[l][r] = True
        # res[r] 表示 s[0~r] 的最小分割次数
        res = [0] * n
        for r in range(n):
            # s[0~r] 为回文，不需要分割
            if dp[0][r]:
                res[r] = 0
            else:
                # s[0~r] 不为回文，最大分割次数为 s[0~r] 所包含字符数 -1，此时， s[0~r] 中不包含回文子串
                res[r] = r
                # 考虑  s[0~r] 中包含回文子串 s[l~r]，此时的分割次数为 s[0~l-1] 的次数+1（s[l~r]只需要额外多1次）
                for l in range(0, r + 1):
                    if dp[l][r]:
                        res[r] = min(res[r], res[l - 1] + 1)
        return res[-1]


def main():
    # s = "aab"
    # s = "a"
    s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    # s = "dcbabce"
    # s = "abc"
    print(Solution().minCut(s))


if __name__ == '__main__':
    main()
