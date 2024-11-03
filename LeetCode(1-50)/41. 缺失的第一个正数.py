"""
将值为n的元素交换到下标为n - 1的位置
如果n - 1位置上的元素值为n,则不交换
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


def main():
    nums = eval(input())
    ob = Solution()
    print(ob.firstMissingPositive(nums))


if __name__ == '__main__':
    main()
