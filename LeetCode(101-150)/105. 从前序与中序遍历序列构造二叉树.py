# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if len(preorder) == 0:
        #     return []
        root = TreeNode(preorder[0])

        def dfs(_left_list: List[int], _right_list: List[int], _root: TreeNode, i: int):
            # 处理左子树
            if len(_left_list) > 0:
                _index = _left_list.index(preorder[i])  # preorder中位置靠前的一定是该子树的根
                _root.left = TreeNode(preorder[i])
                dfs(_left_list[: _index], _left_list[_index + 1:], _root.left, i + 1)
            else:
                _root.left = None

            # 处理右子树
            if len(_right_list) > 0:
                # 找出 preorder 中第一个未被处理的右子树节点
                while preorder[i] not in _right_list:
                    i += 1
                _index = _right_list.index(preorder[i])  # preorder中位置靠前的一定是该子树的根
                _root.right = TreeNode(preorder[i])
                dfs(_right_list[: _index], _right_list[_index + 1:], _root.right, i + 1)
            else:
                _root.right = None

        index = inorder.index(preorder[0])
        # 对中序遍历结果进行进一步划分
        left_list = inorder[: index]
        right_list = inorder[index + 1:]
        dfs(left_list, right_list, root, 1)
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
    # preorder = [3, 9, 20, 15, 7]
    # inorder = [9, 3, 15, 20, 7]
    # preorder = [-1]
    # inorder = [-1]
    # preorder = [1, 2]
    # inorder = [1, 2]
    preorder = [3, 1, 2, 4]
    inorder = [1, 2, 3, 4]
    root = Solution().buildTree(preorder, inorder)
    print_tree(root)
    # Solution().recoverTree(root)
    # print_tree(root)


if __name__ == '__main__':
    main()
