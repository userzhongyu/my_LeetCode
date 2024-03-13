"""
C V
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=(lambda x: x[0]))

        for interval in intervals:
            # 答案集为空或者不存在覆盖区间
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval[:])
            # 存在覆盖区间
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


def main():
    intervals = eval(input())
    print(Solution().merge(intervals))


if __name__ == '__main__':
    main()
