"""
循环n次
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n == 0 or x == 1:
            return res
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        if n < 0:
            n = - n
            x = 1 / x
        for i in range(n):
            res *= x
            if 0 < res < 0.00001:
                return 0
        return round(res, 5)


def main():
    x = eval(input())
    n = eval(input())
    print(Solution().myPow(x, n))


if __name__ == '__main__':
    main()