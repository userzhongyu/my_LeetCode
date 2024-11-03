from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        ans = []
        path = []

        def dfs(k, i):
            if k - len(path) == 0:
                ans.append(path[:])
                return
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(k, j + 1)
                path.pop()

        for l in range(len_nums + 1):
            dfs(l, 0)
            path = []

        return ans


def main():
    nums = eval(input())
    print(Solution().subsets(nums))


if __name__ == '__main__':
    main()
