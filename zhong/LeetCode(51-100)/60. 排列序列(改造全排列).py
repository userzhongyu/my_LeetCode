"""
python中参数为列表、字典、集合时按引用传递;
python中参数为字符串、整数、元组时按值传递;
"""


class Solution:
    def getPermutation(self, n: int, k: int):
        ans = []
        path = [''] * n
        on_path = [False] * n

        def dfs(index: int, count: list):
            if index == n:
                count[0] += 1
                if count[0] == k:
                    ans.append(path[:]) # 解决参数为列表时,引用传递的问题
                return
            if count[0] < k:
                for i in range(n):
                    if not on_path[i]:
                        path[index] = str(i + 1)
                        on_path[i] = True
                        dfs(index + 1, count)
                        on_path[i] = False

        dfs(0, [0])
        return ''.join(ans[0])


def main():
    n = eval(input())
    k = eval(input())
    print(Solution().getPermutation(n, k))


if __name__ == '__main__':
    main()