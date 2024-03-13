from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=(lambda x: [x[0], x[1]]))

        while len(intervals) > 0:
            i = 0
            while i < len(intervals):
                if i < len(intervals) - 1 \
                        and (intervals[i + 1][0] <= intervals[i][1] <= intervals[i + 1][1]
                             or intervals[i][0] <= intervals[i + 1][1] <= intervals[i][1]):
                    intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                    intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                    intervals.remove(intervals[i + 1])
                else:
                    ans.append(intervals[i][:])
                    intervals.remove(intervals[i])

        return ans


def main():
    intervals = eval(input())
    print(Solution().merge(intervals))


if __name__ == '__main__':
    main()
