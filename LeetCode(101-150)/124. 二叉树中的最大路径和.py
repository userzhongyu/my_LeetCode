# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxSum = [root.val]  # 使用一个列表，方便在 dfs 中修改

        def dfs(_root: TreeNode):
            if not _root:
                return 0
            leftSum = max(0, dfs(_root.left))  # 计算左子树的最大路径和，负值则直接舍弃
            rightSum = max(0, dfs(_root.right))  # 计算右子树的最大路径和，负值则直接舍弃
            maxSum[0] = max(maxSum[0], leftSum + rightSum + _root.val)  # 判断最大路径和是否可以从子树中取得，直接影响 maxPathSum 函数的 self.maxSum
            return _root.val + max(leftSum, rightSum)  # 递归选择的前提下，每次只能选择当前节点值与一边子树路径的和

        dfs(root)
        return maxSum[0]


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
    root = [-10, 9, 20, None, None, 15, 7]
    root = build_tree_from_level_order(root)
    print(Solution().maxPathSum(root))


if __name__ == '__main__':
    main()
