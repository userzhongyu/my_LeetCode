from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        M = max(nums)
        m = min(nums)
        avg = max(1, (M - m) // n)  # 计算桶的容量
        res = 0
        buckets = [[] for _ in range((M - m) // avg + 1)]  # 创建桶

        # 装桶
        for i in range(n):
            buckets[(nums[i] - m) // avg].append(nums[i])

        # 计算每个桶的最大最小值
        i = 0
        while i < len(buckets):
            if buckets[i]:
                buckets[i].insert(0, min(buckets[i]))
                buckets[i].append(max(buckets[i]))
                i += 1
            else:
                buckets.pop(i)

        # print(buckets)

        # 计算桶间最大差值
        for i in range(len(buckets) - 1):
            res = max(res, buckets[i + 1][0] - buckets[i][-1])

        return res


def main():
    nums = [3,6,100,4,1,2]
    print(Solution().maximumGap(nums))


if __name__ == '__main__':
    main()
