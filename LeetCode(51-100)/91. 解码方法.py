class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [(int(num)) for num in s]
        dp = [0, 1, ] + [0 for _ in range(len(nums))]

        for i in range(2, len(dp)):
            # 将新加入的一位当做单独的字母
            if nums[i-2] != 0:
                dp[i] += dp[i-1]
                # 将新加入的一位与其前一位组成字母
                if nums[i-2-1] != 0 and nums[i-2-1]*10+nums[i-2] <= 26:
                    dp[i] += dp[i-2]
            # 新加入的一位为0且能与其前一位组成字母
            elif nums[i-2-1] != 0 and nums[i-2-1]*10 <= 26:
                dp[i] = dp[i-2]
            else:
                break
        return dp[-1]


def main():
    # s = '11106'
    # s = '12'
    # s = '10'
    # s = '00'
    s = '230'
    print(Solution().numDecodings(s))


if __name__ == '__main__':
    main()
