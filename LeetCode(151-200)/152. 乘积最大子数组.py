from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        imax = 1
        imin = 1
        maxmul = nums[0]
        for i in range(n):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            maxmul = max(maxmul, imax)
        return maxmul


def main():
    nums = [2, 3, -2, 4]  # 6
    # nums = [-2, 0, -1]  # 0
    # nums = [1]
    nums = [-5, 2, 4, 1, -2, 2, -6, 3, -1, -1, -1, -2, -3, 5, 1, -3, -4, 2, -4, 6, -1, 5, -6, 1, -1, -1]
    print(Solution().maxProduct(nums))


if __name__ == '__main__':
    main()
