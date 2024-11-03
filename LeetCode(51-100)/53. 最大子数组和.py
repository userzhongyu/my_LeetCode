from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = max(nums)
        right = 0
        count = 0
        while right < n:
            count += nums[right]
            if count < 0:
                left = right + 1
                right = left
                count = 0
            else:
                ans = max(ans, count)
                right += 1
        return ans


def main():
    nums = eval(input())
    print(Solution().maxSubArray(nums))


if __name__ == '__main__':
    main()