import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dic = {}
        n = len(points)
        if n == 1:
            return 1
        for i in range(n):
            for j in range(i+1, n):
                temp = self.calculate(points[i], points[j])
                if temp not in dic:
                    dic[temp] = 1
                else:
                    dic[temp] += 1
        x = max(dic.values())
        x = 2 * x
        for i in range(1, n + 1):
            if i * (i - 1) == x:
                return i


    def calculate(self, p1, p2):
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        if x1 == x2:
            k = math.inf
            b = x1
            return str([k, b])
        elif y1 == y2:
            k = 0
            b = y1
        else:
            k = (y2 - y1) / (x2 - x1)
            b = y1 - k * x1
        k = round(k, 8)
        b = round(b, 8)
        return str([k ,b])


def main():
    # points = [[1, 1], [2, 2], [3, 3]]
    # points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    # points = [[1, 1]]
    # points = [[2,3],[3,3],[-5,3]]
    points = [[-6,-1],[3,1],[12,3]]
    # points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
    print(Solution().maxPoints(points))


if __name__ == '__main__':
    main()
