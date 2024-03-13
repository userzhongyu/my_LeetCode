"""
https://leetcode.cn/problems/wildcard-matching/solutions/316462/yi-ge-qi-pan-kan-dong-dong-tai-gui-hua-dpsi-lu-by-/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # # 边界值处理
        # if s_len == 0:
        #     if p == s or set(p) == {'*'}:
        #         return True
        #     else:
        #         return False

        dp = [[False] * (s_len + 1) for _ in range(0, p_len + 1)]

        # 哨兵
        dp[0][0] = True
        # # if p[0] == '*':   # 存在len(p) == 0产生的异常
        # if p.startswith('*'):
        #     dp[1] = [True] * (s_len + 1)

        for p_i in range(1, p_len + 1):
            # 处理1.以'*'开始 2.以'*'开始并存在连续的'*'的情况
            if p[p_i - 1] == '*' and dp[p_i - 1][0]:
                dp[p_i] = [True] * (s_len + 1)
            else:
                for s_j in range(1, s_len + 1):
                    if p[p_i - 1] in {s[s_j - 1], '?'}:
                        dp[p_i][s_j] = dp[p_i - 1][s_j - 1]
                    elif p[p_i - 1] == '*' and dp[p_i - 1][s_j]:
                        for s_temp in range(s_j, s_len + 1):
                            dp[p_i][s_temp] = True
                        break

        return dp[p_len][s_len]


def main():
    s = eval(input())
    p = eval(input())
    ob = Solution()
    print(ob.isMatch(s, p))


if __name__ == '__main__':
    main()
