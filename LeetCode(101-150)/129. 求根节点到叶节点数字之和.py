# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = [0, ]

        def dfs(cur: TreeNode, num):
            if not (cur.left or cur.right):
                total[0] += num
                return
            if cur.left:
                dfs(cur.left, num * 10 + cur.left.val)
            if cur.right:
                dfs(cur.right, num * 10 + cur.right.val)

        dfs(root, root.val)
        return total[0]


# 层序遍历构建二叉树
def build_tree_from_level_order(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])  # 创建根节点
    queue = [root]
    index = 1

    while index < len(level_order):
        node = queue.pop(0)  # 取出当前节点
        if level_order[index] is not None:  # 如果左子节点存在
            node.left = TreeNode(level_order[index])
            queue.append(node.left)
        index += 1

        if index < len(level_order) and level_order[index] is not None:  # 如果右子节点存在
            node.right = TreeNode(level_order[index])
            queue.append(node.right)
        index += 1

    return root


# 打印树的层序遍历，验证结果
from collections import deque


def print_tree(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def main():
    # root = [1, 2, 3]
    # root = [4, 9, 0, 5, 1]
    root = [0, 1]
    root = build_tree_from_level_order(root)
    print(Solution().sumNumbers(root))


if __name__ == '__main__':
    main()
