# Definition for a binary tree node.
from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dsf(_min_node: TreeNode, _max_node: TreeNode, _root: TreeNode):
            if not _root:
                return
            if _min_node.val < _root.val < _max_node.val:
                dsf(_min_node, _root, _root.left)  # 判断左子树
                dsf(_root, _max_node, _root.right)  # 判断右子树
            elif _min_node.val > _root.val:
                tmp = _min_node.val
                _min_node.val = _root.val
                _root.val = tmp
            elif _max_node.val < _root.val:
                tmp = _max_node.val
                _max_node.val = _root.val
                _root.val = tmp

        def judge(_min: int, _max: int, _root: TreeNode):
            if not _root:
                return TreeNode
            return _min < _root.val < _max and judge(_min, _root.val, _root.left) and judge(_root.val, _max, _root.right)

        min_node = TreeNode(-math.inf)
        max_node = TreeNode(math.inf)
        while not judge(min_node.val, max_node.val, root):
            dsf(min_node, max_node, root)


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
    # root = [1, 3, None, None, 2]
    root = [2, 3, 1]
    root = build_tree_from_level_order(root)
    print_tree(root)
    Solution().recoverTree(root)
    print()
    print_tree(root)


if __name__ == '__main__':
    main()
