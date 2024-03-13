from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(temp: List[int], path: List[int]):
            if len(path) == n:
                res.append(path[:])
                return
            # 减少备选元素
            for index in range(0, len(temp)):
                tmp = temp[index]
                path.append(tmp)
                temp.remove(tmp)
                dfs(temp, path)
                path.pop()
                temp.insert(index, tmp)

        dfs(nums, [])
        return res


def main():
    nums = eval(input())
    print(Solution().permute(nums))


if __name__ == '__main__':
    main()


