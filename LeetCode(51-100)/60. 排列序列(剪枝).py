"""
当前分支的排列组合个数为其叶子数,即当前未排序数目的阶乘
根据k与当前结点的叶子数的关系判断是否进入该分支
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
                    ans.append(path[:])
                return
            if count[0] < k:
                for i in range(n):
                    if not on_path[i]:
                        # 计算当前节点所有叶子数
                        temp = 1
                        for j in range(n - index - 1, 0, -1):
                            temp *= j
                        if count[0] + temp < k:
                            count[0] += temp
                        else:
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