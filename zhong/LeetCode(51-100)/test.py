from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            return nums
        return solve(2)


def main():
    nums = eval(input())
    print(Solution().removeDuplicates(nums))


if __name__ == '__main__':
    main()