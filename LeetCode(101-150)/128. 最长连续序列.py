from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxl = 0
        setnums = set(nums)

        for left in setnums:
            if left - 1 in setnums:
                continue  # 当前操作数不能作为一组连续序列的开头
            right = left + 1
            # 判断以当前操作数为开头的序列有多长
            while right in setnums:
                right += 1
            maxl = max(maxl, right - left)  # 由于是序列连续，所以可以直接通过 right - left 得出序列长度

        return maxl


def main():
    # nums = [100, 4, 200, 1, 3, 2]
    nums = [1, 0, -1]
    # nums = [0, -1]
    print(Solution().longestConsecutive(nums))


if __name__ == '__main__':
    main()
