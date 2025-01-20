import math
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, hight = 0, len(nums) - 1
        while low < hight:
            mid =  (low + hight) // 2
            if nums[mid] > nums[mid + 1]:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    hight = mid
            else:
                low = mid + 1
        return (low + hight) // 2  # 返回最新的mid


def main():
    # nums = [1,2,1,3,5,6,4]
    # nums = [1, 2, 3, 1]
    # nums = [1]
    # nums = [1, 2, 3, 4]
    # nums = [3, 2, 1, -1]
    nums = [1, 2]
    # nums = [4, 3, 2, 1, 4]

    print(Solution().findPeakElement(nums))


if __name__ == '__main__':
    main()
