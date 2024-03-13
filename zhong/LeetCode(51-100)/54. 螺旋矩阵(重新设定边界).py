from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = -1
        down = len(matrix)
        left = -1
        right = len(matrix[0])
        sum = right * down
        ans = []

        i = j = 0
        count = 0

        while count < sum:
            # 左
            while j < right and count < sum:
                ans.append(matrix[i][j])
                count += 1
                j += 1
            j -= 1
            i += 1
            up += 1
            # 下
            while i < down and count < sum:
                ans.append(matrix[i][j])
                count += 1
                i += 1
            i -= 1
            j -= 1
            right -= 1
            # 右
            while j > left and count < sum:
                ans.append(matrix[i][j])
                count += 1
                j -= 1
            j += 1
            i -= 1
            down -= 1
            # 上
            while i > up and count < sum:
                ans.append(matrix[i][j])
                count += 1
                i -= 1
            i += 1
            j += 1
            left += 1
        return ans


def main():
    matrix = eval(input())
    print(Solution().spiralOrder(matrix))


if __name__ == '__main__':
    main()
