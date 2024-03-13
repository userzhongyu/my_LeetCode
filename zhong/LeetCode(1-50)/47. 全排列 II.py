from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        def dfs(temp: List[int], now: List[int]):
            if len(temp) == 0:
                if now not in res:
                    res.append(now[:])
                return
            for index in range(0, len(temp)):
                tmp = temp[index]
                now.append(tmp)
                temp.remove(tmp)
                dfs(temp, now)
                now.pop()
                temp.insert(index, tmp)

        dfs(nums, [])
        return res


def main():
    nums = eval(input())
    print(Solution().permute(nums))


if __name__ == '__main__':
    main()


