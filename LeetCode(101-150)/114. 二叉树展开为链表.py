# Definition for a binary tree node.
import copy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(_root: TreeNode):
            if not _root:
                return
            # 从最左下开始，改变树的结构
            if _root.left:
                dfs(_root.left)
            if _root.right:
                _node = _root
                # 找到最左下的节点
                while _node:
                    _left = _node
                    _node = _node.left
                # 将当前节点的右子节点放到最左下节点的左子节点
                _left.left = _root.right
                _root.right = None
                dfs(_left)

        dfs(root)
        node = root
        while node:
            node.right = node.left
            node.left = None
            node = node.right


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
    root = [1, 2, 5, 3, 4, None, 6]
    root = build_tree_from_level_order(root)
    # print_tree(root)
    Solution().flatten(root)
    print_tree(root)
    # print_tree(root)


if __name__ == '__main__':
    main()
