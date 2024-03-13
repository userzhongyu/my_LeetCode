from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        flag = False  # 标记是否已经插入区间

        for interval in intervals:
            if flag:
                ans.append(interval[:])
            else:
                if interval[1] < newInterval[0]:
                    ans.append(interval[:])
                # 添加左边区间
                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                if interval[0] > newInterval[1]:
                    ans.append(newInterval[:])
                    ans.append(interval)
                    flag = True
                # 添加右边区间
                else:
                    newInterval[1] = max(newInterval[1], interval[1])
        # 插入末尾
        if not flag:
            ans.append(newInterval[:])
        return ans


def main():
    intervals = eval(input())
    newInterval = eval(input())
    print(Solution().insert(intervals, newInterval))


if __name__ == '__main__':
    main()