from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, hight = 0 , len(nums) - 1
        while low < hight:
            mid = (low + hight) // 2
            # 尽量去数组后半段寻找
            if nums[mid] < nums[hight]:
                hight = mid
            else:
                low = mid + 1
        return nums[low]


def main():
    nums = [3, 4, 5, 1, 2]  # 1
    # nums = [4, 5, 6, 7, 0, 1, 2]  # 0
    # nums = [11, 13, 15, 17]  # 11
    # nums = [4, 5, 1, 2, 3]
    # nums = [1]
    print(Solution().findMin(nums))


if __name__ == '__main__':
    main()
