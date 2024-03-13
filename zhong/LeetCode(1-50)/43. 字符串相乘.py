class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = int(num1)
        res = 0
        n = len(num2)
        for i in range(n - 1, -1, -1):
            res += num1 * int(num2[i]) * (10 ** (n - i - 1))
        return str(res)


def main():
    num1 = eval(input())
    num2 = eval(input())
    ob = Solution()
    print(ob.multiply(num1, num2))


if __name__ == '__main__':
    main()