"""
@Time ： 2024/7/21 下午4:15
@Auth ： user_zhong
"""
import json
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [['0'] + [str(element) for element in row] + ['0'] for row in matrix]  # 添加哨兵
        n = len(matrix)
        m = len(matrix[0])

        heights = [0] * m
        ans = 0

        for i in range(n):
            # 计算高度
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # 转换成84题
            stack = [0]
            for j in range(1, m):
                while heights[j] < heights[stack[-1]]:
                    cur_heights = heights[stack.pop()]
                    cur_width = j - stack[-1] - 1
                    ans = max(ans, cur_heights * cur_width)

                stack.append(j)

        return ans



data = input("输入：")
data = json.loads(data)
matrix = [[str(element) for element in row] for row in data]
print(matrix)
ans = Solution().maximalRectangle(matrix)
print(ans)

