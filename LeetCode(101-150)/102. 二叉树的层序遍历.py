# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        ans = []
        out = []
        h = []
        if root:
            queue.append(root)
            h.append(1)
        else:
            return ans
        i = 0
        while i < len(queue):
            node = queue[i]
            out.append(node.val)
            if node.left:
                queue.append(node.left)
                h.append(h[i] + 1)
            if node.right:
                queue.append(node.right)
                h.append(h[i] + 1)

            i += 1

        # print(h)
        tmp = []
        for i in range(len(out)):
            if not tmp:
                tmp.append(out[i])
            elif i > 0 and h[i] == h[i - 1]:
                tmp.append(out[i])
            else:
                ans.append(tmp[:])
                tmp = [out[i]]
        ans.append(tmp[:])

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
    # root = [2, 3, 1]
    root = [3, 9, 20, None, None, 15, 7]
    root = build_tree_from_level_order(root)
    # print_tree(root)
    # Solution().recoverTree(root)
    print(Solution().levelOrder(root))
    # print_tree(root)


if __name__ == '__main__':
    main()
