from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, hight = 0, len(nums) - 1
        while low < hight:
            mid = (low + hight) // 2
            # 遇到值相同的情况，缩小判断区间
            if nums[mid] == nums[hight]:
                hight -= 1
            elif nums[mid] < nums[hight]:
                hight = mid
            else:
                low = mid + 1

        return nums[low]


def main():
    nums = [2, 2, 2, 0, 1]
    # nums = [1, 3, 3]
    # nums = [3,3,1,3]
    nums = [3,3,1,3,3,3,3]

    print(Solution().findMin(nums))


if __name__ == '__main__':
    main()
