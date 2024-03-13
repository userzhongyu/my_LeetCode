from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last = len(matrix[0]) - 1
        for i in range(0, len(matrix)):
            if target <= matrix[i][last]:
                return self.mySort(matrix[i], target)
        return False

    def mySort(self, lst, target):
        right = len(lst) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                return True
            elif lst[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


def main():
    matrix = eval(input())
    target = eval(input())
    print(Solution().searchMatrix(matrix, target))


if __name__ == '__main__':
    main()