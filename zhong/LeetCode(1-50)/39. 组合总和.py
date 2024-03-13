"""
C V
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)

        def dfs(now: list[int], index: int) -> None:
            if sum(now) == target:
                res.append(now[:])
                # res.append(now)
                # #append()函数追加的是对象的引用,导致结果出错
                # 参考:https://blog.csdn.net/u010099495/article/details/50276833
                # 要解决这个问题，需要对now进行深拷贝后append到result中。而list(now)就会返回now的一个深拷贝。
                # 除了用list(now)以外，还可以用now[:]进行深拷贝。
                return
            if sum(now) > target:
                return

            for i in range(index, n):
                now.append(candidates[i])
                dfs(now, i)
                now.pop()
        dfs([], 0)
        return res


def main():
    candidates = eval(input())
    target = int(input())
    ob = Solution()
    print(ob.combinationSum(candidates, target))


if __name__ == '__main__':
    main()