from typing import List
"""
剪枝
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            # 同一层不要出现重复的数字
            # 出现重复的数字时,会从后往前逐个除去该数字,仅保留一个
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 去掉nums[i]之后的数组
            pre = self.permuteUnique(nums[:i] + nums[i+1:])
            # 在各个组合之间加上nums[i]
            for lst in pre:
                res.append([nums[i]] + lst)
        return res


def main():
    nums = eval(input())
    print(Solution().permuteUnique(nums))


if __name__ == '__main__':
    main()


