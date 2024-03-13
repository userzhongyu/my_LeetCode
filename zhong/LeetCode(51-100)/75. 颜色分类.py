from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index0 = 0
        index2 = len(nums) - 1
        i = 0
        while i <= index2:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[index0]
                nums[index0] = temp
                index0 += 1
            elif nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[index2]
                nums[index2] = temp
                index2 -= 1
                i -= 1
            i += 1


def main():
    nums = eval(input())
    Solution().sortColors(nums)
    print(nums)


if __name__ == '__main__':
    main()