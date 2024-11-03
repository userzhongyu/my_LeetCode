"""
@Time ： 2024/7/27 下午9:07
@Auth ： user_zhong
"""


class Solution:
    def isScramble(self, s1, s2):  # 判断s2是不是s1的扰乱字符串
        lens1 = len(s1)
        lens2 = len(s2)
        if lens1 != lens2:
            return False
        # 初始化dp3维数组dp[i][j][k]
        # i为0~lens1-1共lens1个， j为0~lens1-1共lens1个， k为1~lens1+1共lens1个
        dp = [[[False] * (lens1 + 1) for _ in range(lens1)] for _ in range(lens1)]

        # 初始化单个字符的情况
        for i in range(lens1):
            for j in range(lens1):
                dp[i][j][1] = s1[i] == s2[j]

        # 前面排除了s1和s2为单个字符的情况，那么我们就要划分区间了，k从2到lens1，也就是划分为s1[:k]和s1[k:]

        # 枚举区间长度2～lens1
        for k in range(2, lens1 + 1):
            # 枚举S中的起点位置
            for i in range(lens1 - k + 1):  # 也就是在s1中枚举i的位置，因为后面会出现i+w的情况，而w最大就是k，
                # 就会有i+k的情况，所以i的取值范围就是0~lens1-k

                # 枚举T中的起点位置
                for j in range(lens1 - k + 1):
                    # 枚举划分位置，s1[:k]中从
                    for w in range(1, k):
                        # 第一种情况：S1->T1,S2->T2
                        if dp[i][j][w] and dp[i + w][j + w][k - w]:
                            dp[i][j][k] = True
                            print("i,j,k", i, j, k)
                            break

                        # 第二种情况：S1->T2,S2->T1
                        # S1起点i，T2起点j + 前面那段长度k-w，S2起点i+前面长度k
                        if dp[i][j + k - w][w] and dp[i + w][j][k - w]:
                            dp[i][j][k] = True
                            print("i,j,k", i, j, k)
                            break
        return dp[0][0][lens1]

def main():
    s1 = input("s1:")
    s2 = input("s2:")
    ans = Solution().isScramble(s1, s2)
    print(ans)


if __name__ == '__main__':
    main()
