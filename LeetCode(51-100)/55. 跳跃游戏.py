from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        left = 0
        right = nums[0]

        while right < n - 1:
            start = left
            end = right + 1
            for i in range(start, end):
                if i + nums[i] > right:
                    right = i + nums[i]
            # 可跳跃区间没有发生改变
            if end == right + 1:
                return False
            left = end

        return True


def main():
    nums = eval(input())
    print(Solution().canJump(nums))


if __name__ == '__main__':
    main()