"""
C V
"""
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break
                # 在一个for循环中，所有被遍历到的数都是属于一个层级的
                # 我们要让一个层级中，出现的数字均不相同
                # 由于经过了排序,所以相同的数会连续排列 只保留第一个
                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                # candidates == [a,a,b,b]
                #        r
                #     / | | \
                #    a  a b  b
                # 第一个b因为candidates[index - 1] != candidates[index],所以继续运行
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res


def main():
    candidates = eval(input())
    target = int(input())
    ob = Solution()
    print(ob.combinationSum2(candidates, target))


if __name__ == '__main__':
    main()