from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            d = k - len(path)

            if d == 0:
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()

        dfs(n)

        return ans


def main():
    n = eval(input())
    k = eval(input())
    print(Solution().combine(n ,k))


if __name__ == '__main__':
    main()
