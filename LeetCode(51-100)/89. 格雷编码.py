import math
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]
        # 一轮一轮生成
        for i in range(1, n):
            temp = []  # 增加的新列表
            for j in range(1, len(ans)+1):
                temp.append(ans[-j]+pow(2, i))  # 总结出来的规律
            ans.extend(temp)
        return ans


def main():
    n = 4
    print(Solution().grayCode(n))


if __name__ == '__main__':
    main()
