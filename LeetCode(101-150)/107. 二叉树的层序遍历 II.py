# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        ans = []
        out = []
        h = []

        if not root:
            return ans
        queue.append(root)
        out.append(root.val)
        h.append(1)

        i = 0
        while i < len(queue):
            tmp_node = queue[i]
            if tmp_node.left:
                queue.append(tmp_node.left)
                out.append(tmp_node.left.val)
                h.append(h[i] + 1)
            if tmp_node.right:
                queue.append(tmp_node.right)
                out.append(tmp_node.right.val)
                h.append(h[i] + 1)
            i += 1

        # print(out)
        # print(h)
        tmp_list = []
        for i in range(len(out)):
            if not tmp_list:
                tmp_list.append(out[i])
            elif h[i] != h[i - 1]:
                ans.insert(0, tmp_list[:])
                tmp_list = [out[i]]
            else:
                tmp_list.append(out[i])
        ans.insert(0, tmp_list)
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
    print(Solution().levelOrderBottom(root))
    # print_tree(root)


if __name__ == '__main__':
    main()
