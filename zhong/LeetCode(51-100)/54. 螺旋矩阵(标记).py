from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        c = len(matrix[0])
        r = len(matrix)
        ans = []

        flag = [[False] * c for _ in range(r)]
        count = i = j = 0

        while count < c * r:
            # 左
            while j < c and not flag[i][j]:
                ans.append(matrix[i][j])
                flag[i][j] = True
                count += 1
                j += 1
            j -= 1
            i += 1
            # 下
            while i < r and not flag[i][j]:
                ans.append(matrix[i][j])
                flag[i][j] = True
                count += 1
                i += 1
            i -= 1
            j -= 1
            # 右
            while j >= 0 and not flag[i][j]:
                ans.append(matrix[i][j])
                flag[i][j] = True
                count += 1
                j -= 1
            j += 1
            i -= 1
            # 上
            while i >= 0 and not flag[i][j]:
                ans.append(matrix[i][j])
                flag[i][j] = True
                count += 1
                i -= 1
            i += 1
            j += 1
        return ans


def main():
    matrix = eval(input())
    print(Solution().spiralOrder(matrix))


if __name__ == '__main__':
    main()
