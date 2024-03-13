"""
C V
贪心算法：找出下一步能到的区间，并从区间中取出下下一步能到达最远位置的点作为下一步到达的点
https://leetcode.cn/problems/jump-game-ii/solutions/1022501/tan-xin-suan-fa-si-lu-qing-xi-by-wonderf-avua/
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        # 边界处理
        if length == 1:
            return 0
        left, right = 1, nums[0]
        step = 1
        while right < length - 1:
            # 遍历当前能到达的所有点，取出下一次能到达的最远位置的点，并用left和right记录该点下一次能到达的区间
            for i in range(left, right + 1):
                # 找出最大值作为下一区间的right
                if nums[i] + i > right:
                    right = nums[i] + i
                    left = i + 1
            # 每次找出新的区间,就进行一次跳跃
            step += 1

        return step


def main():
    nums = eval(input())
    ob = Solution()
    print(ob.jump(nums))


if __name__ == '__main__':
    main()

