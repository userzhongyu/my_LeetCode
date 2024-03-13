"""
二分法
https://leetcode.cn/problems/powx-n/solutions/241471/50-powx-n-kuai-su-mi-qing-xi-tu-jie-by-jyd/
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 or x == 1:
            return 1
        if x == -1:
            if n % 2 == 1:
                return -1
            else:
                return 1
        res = 1
        if n < 0:
            n = - n
            x = 1 / x
        while n:
            if n % 2 == 1:
                res *= x
            n = n // 2
            x *= x
        return res


def main():
    x = eval(input())
    n = eval(input())
    print(Solution().myPow(x, n))


if __name__ == '__main__':
    main()