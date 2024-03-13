"""
C V
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # dp[i][j] 表示s[0:i]与p[0:j]是否匹配(左闭右开)
        dp = [[False] * (p_len + 1) for _ in range(0, s_len + 1)]  # 初始状态,默认值为False
        dp[0][0] = True  # 哨兵

        # s 为空串
        for j in range(1, p_len + 1):
            # 若 p 的第 j 个字符 p[j] 是 '*'
            # 说明p[j - 1]、p[j] 个可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # 为dp赋值
        for i in range(1, s_len + 1):
            # 检查s[0:i]与p[0:j]是否匹配
            for j in range(1, p_len + 1):
                # p[j - 1]与s[i - 1]匹配,检查s[0:i - 1]与p[0:j - 1]
                # if p[j - 1] != '*':
                #     dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                # 优化写法
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                # p[j - 1]是'*',根据情况赋值
                elif p[j - 1] == '*':
                    # p[j - 2]与s[i - 2]匹配
                    if p[j - 2] in {s[i - 1], '.'}:
                        # dp[i][j - 2]代表'*'让p[j - 2]重复0遍(消去p[j - 1])
                        # dp[i][j - 1]代表'*'让p[j - 2]重复1遍
                        # dp[i - 1][j]代表'*'让p[j - 2]重复2遍及以上,消去s[i - 1] 重新匹配
                        # dp[i][j] = dp[i][j - 2] or dp[i][j - 1] or dp[i - 1][j]
                        # -------------------------------------------------------------
                        # 由于p[j - 2]与s[i - 1]相匹配
                        # 所以 dp[i][j - 1]代表'*'让p[j - 2]重复1遍 可以进一步可以演化成 1.消去s[i - 1] 2.'*'让p[j - 2]重复0次 的操作
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    # p[j - 1]为'*'可以消去p[j - 2],重新匹配
                    else:
                        dp[i][j] = dp[i][j - 2]
                # 如果p[j - 1]不是'*'且与s[i - 1]不匹配,则dp[i][j]取默认值False
                # else:
                #     dp[i][j] = False
        return dp[s_len][p_len]


def main():
    s = eval(input())
    p = eval(input())
    ob = Solution()
    print(ob.isMatch(s, p))


if __name__ == '__main__':
    main()
