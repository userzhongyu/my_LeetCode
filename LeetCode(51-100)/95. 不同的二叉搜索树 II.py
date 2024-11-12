# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 题解
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(l, r):
            if l > r:
                return [None]
            ans = []  # 从l到r的搜索树集合
            # 选子树的根节点
            for i in range(l, r + 1):
                # 选一棵左子树
                for x in dfs(l, i - 1):
                    # 选一棵右子树
                    for y in dfs(i + 1, r):
                        # 以当前元素为根节点
                        root = TreeNode(i)
                        # 拼接上左子树和右子树
                        root.left, root.right = x, y
                        ans.append(root)  # 只需要将树的头节点放入列表
            return ans

        return dfs(1, n)


def main():
    n = 5
    ans = Solution().generateTrees(n)
    print(len(ans))
    # for i in range(len(ans)):
    #     print('[', end='')
    #     for j in range(len(ans[i])):
    #         print(ans[i][j].val, end=',')
    #     print(']')
    # for i in range(len(ans)):
    #     print(ans[i].val)
    # print(ans[2].left.val)


if __name__ == '__main__':
    main()
