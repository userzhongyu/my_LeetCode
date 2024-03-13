class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        out = 0
        while temp > 0:
            out = out * 10 + temp % 10
            temp = temp // 10
        if x < 0:
            out = out * (-1)
        if out > 2 ** 31 - 1 or out < 2 ** 31 * -1:
            return 0
        else:
            return out


def main():
    x = int(input())
    print(Solution().reverse(x))


if __name__ == '__main__':
    main()
