"""
递归
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        # 一些变量可以直接取得
        def backtrack(left: int, right: int, temp):
            # 递归出口
            if right == n:
                res.append(temp)
                return
            if left < n:
                # 先加入一个'('
                temp += '('
                # 深入
                backtrack(left + 1, right, temp)
                # 删除所添加的'('
                temp = temp[0: -1]
            if left > right:
                # 先加入一个')'
                temp += ')'
                # 深入
                backtrack(left, right + 1, temp)
                # 删除所添加的')'
                temp = temp[0: -1]

        # 调用函数
        backtrack(0, 0, '')
        return res


def main():
    ob = Solution()
    n = int(input())
    print(ob.generateParenthesis(n))


if __name__ == '__main__':
    main()
