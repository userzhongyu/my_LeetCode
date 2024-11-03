from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def biFind(left, right):
            if left > right:
                return False
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            return biFind(left, mid - 1) or biFind(mid + 1, right)

        return biFind(0, len(nums) - 1)


def main():
    nums = eval(input())
    target = eval(input())
    print(Solution().search(nums, target))


if __name__ == '__main__':
    main()
