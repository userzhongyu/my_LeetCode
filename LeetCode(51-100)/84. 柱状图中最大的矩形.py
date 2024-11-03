"""
@Time ： 2024/7/19 上午10:12
@Auth ： user_zhong
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights = [0] + heights + [0]  # 添加哨兵，防止越界
        size = len(heights)
        stack = [0]  # 存储索引下标

        for i in range(1, size):
            # 从右往左找到比当前栈顶小的元素的个数，作为宽
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]  # 取完柱子高度后，将该柱子下标出栈，栈顶元素为左边挨得最近的矮柱子下标
                cur_width = i - stack[-1] - 1  # 计算宽度左边界的时候，应找到挨得最近且高度小于当前柱子的元素
                ans = max(ans, cur_height * cur_width)

            # 经过上述处理，可以保证栈内所存元素对应高度不减
            stack.append(i)

        return ans

def main():
    str = input("输入:").split(' ')
    heights = [int(item) for item in str]
    ans = Solution().largestRectangleArea(heights)
    print(ans)


if __name__ == '__main__':
    main()

