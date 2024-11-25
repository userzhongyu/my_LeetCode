# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(_root: Optional[TreeNode], _path: list, _sum: int):
            if not _root:
                return
            elif _sum + _root.val == targetSum and not _root.left and not _root.right:
                _path.append(_root.val)
                ans.append(_path[:])
                _path.pop()  # 恢复现场
                return
            else:
                _path.append(_root.val)
                _sum += _root.val
                dfs(_root.left, _path, _sum)
                dfs(_root.right, _path, _sum)
                _path.pop()  # 恢复现场

        dfs(root, [], 0)
        return ans


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


def main():
    # root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    # targetSum = 22
    # root = [1, 2, 3]
    # targetSum = 5
    root = [-2, None, -3]
    targetSum = -5
    root = build_tree_from_level_order(root)
    print(Solution().pathSum(root, targetSum))


if __name__ == '__main__':
    main()
