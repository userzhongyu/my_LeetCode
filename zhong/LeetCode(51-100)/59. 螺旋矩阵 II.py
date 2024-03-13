from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[-1] * n for _ in range(n)]
        up = -1
        down = n
        left = -1
        right = n

        num = 1
        i = 0
        j = -1
        while num <= n * n:
            while j < right - 1:
                j += 1
                ans[i][j] = num
                num += 1
            up += 1
            while i < down - 1:
                i += 1
                ans[i][j] = num
                num += 1
            right -= 1
            while j > left + 1:
                j -= 1
                ans[i][j] = num
                num += 1
            down -= 1
            while i > up + 1:
                i -= 1
                ans[i][j] = num
                num += 1
            left += 1
        return ans


def main():
    n = eval(input())
    print(Solution().generateMatrix(n))


if __name__ == '__main__':
    main()
