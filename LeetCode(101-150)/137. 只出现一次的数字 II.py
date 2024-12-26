from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for item in nums:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        for item in dic:
            if dic[item] == 1:
                return item


def main():
    nums = [2, 2, 3, 2]
    print(Solution().singleNumber(nums))


if __name__ == '__main__':
    main()
