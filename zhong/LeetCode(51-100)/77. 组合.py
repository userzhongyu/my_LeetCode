from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = [x for x in range(1, n + 1)]
        ans = []

        def dfs(path):
            if len(path) == k:
                ans.append(path[:])
                return
            for index, item in enumerate(lst):
                if path == [] or item > path[-1]:
                    path.append(item)
                    lst.remove(item)
                    dfs(path)
                    path.pop()
                    lst.insert(index, item)
        dfs([])
        return ans


def main():
    n = eval(input())
    k = eval(input())
    print(Solution().combine(n ,k))


if __name__ == '__main__':
    main()

