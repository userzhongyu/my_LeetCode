from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


def main():
    nums = eval(input())
    print(Solution().removeDuplicates(nums))


if __name__ == '__main__':
    main()
