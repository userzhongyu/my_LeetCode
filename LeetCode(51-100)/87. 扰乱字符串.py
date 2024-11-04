"""
@Time ： 2024/7/27 下午9:07
@Auth ： user_zhong
"""
import numpy as np

class Solution:
    def isScramble(self, s1, s2):  # 判断s2是不是s1的扰乱字符串
        lens1 = len(s1)

        dp = [[[False]*(lens1+1) for _ in range(lens1)] for _ in range(lens1)]
        print(dp)
        print(np.array(dp).shape)
        # 先判断单个字母的是否匹配
        for i in range(lens1):
            for j in range(lens1):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for l in range(2, lens1+1):
            for i in range(lens1-l+1):
                for j in range(lens1-l+1):
                    # 子片段
                    for temp in range(1, l):
                        if dp[i][j][temp] and dp[i+temp][j+temp][l-temp]:
                            dp[i][j][l] = True
                        if dp[i][j+l-temp][temp] and dp[i+temp][j][l-temp]:
                            dp[i][j][l] = True

        return dp[0][0][lens1]


def main():
    # s1 = input("s1:")
    # s2 = input("s2:")
    s1 = "abcdefghijklmnopq"
    s2 = "efghijklmnopqcadb"
    ans = Solution().isScramble(s1, s2)
    print(ans)


if __name__ == '__main__':
    main()
