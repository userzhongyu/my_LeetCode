"""
dfs
超时
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1

        def dfs(now: int, step: int, min_jump: list, count: int):
            if now >= end:
                min_jump[0] = min(min_jump[0], count)
                return

            for i in range(step, 0, -1):
                if i + now > end:
                    temp = end
                else:
                    temp = now + i
                # 假设先进行跳跃
                count += 1
                # 进入下一个状态
                dfs(temp, nums[temp], min_jump, count)
                # 回到上一个状态,进行另外的跳跃
                count -= 1

        res = [len(nums)]
        dfs(0, nums[0], res, 0)
        return res[0]


def main():
    nums = eval(input())
    ob = Solution()
    print(ob.jump(nums))


if __name__ == '__main__':
    main()

