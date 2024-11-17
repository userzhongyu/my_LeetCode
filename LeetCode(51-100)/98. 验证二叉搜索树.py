from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], _min=-math.inf, _max=math.inf) -> bool:
        if not root:
            return True
        return _min < root.val < _max and self.isValidBST(root.left, _min, root.val) and self.isValidBST(root.right, root.val, _max)


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
    # root = [5, 4, 6, None, None, 3, 7]
    # root = [26, 19, None, 27]
    root = [32, 26, 47, 19, None, None, 56, None, 27]
    root = build_tree_from_level_order(root)
    # print_tree(root)
    print(Solution().isValidBST(root))


if __name__ == '__main__':
    main()
