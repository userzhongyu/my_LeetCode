from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()  # 排序，使得相同元素相邻
        self.dfs(ans, path, nums, 0)
        return ans

    def dfs(self, ans: list, path: list, nums: List[int], i: int):
        ans.append(path[:])  # 深拷贝
        if i == len(nums):
            return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            path.append(nums[j])
            self.dfs(ans, path, nums, j+1)  # 本轮次已经操作到第j个元素，下一轮次从j+1开始操作
            path.pop()


def main() -> object:
    # nums = [1, 4, 3, 5, 4, 4, 7, 7, 8, 0]
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()
