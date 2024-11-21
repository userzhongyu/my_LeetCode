# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(_left_list: List[int], _right_list: List[int], _root: TreeNode, i: int):
            # 先处理右子树
            if len(_right_list) > 0:
                _index = _right_list.index(postorder[i])
                _root.right = TreeNode(postorder[i])
                dfs(_right_list[: _index], _right_list[_index + 1:], _root.right, i - 1)
            else:
                _root.right = None
            # 再处理左子树
            if len(_left_list) > 0:
                while postorder[i] not in _left_list:
                    i -= 1
                _index = _left_list.index(postorder[i])
                _root.left = TreeNode(postorder[i])
                dfs(_left_list[: _index], _left_list[_index + 1:], _root.left, i - 1)
            else:
                _root.left = None

        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        left_list = inorder[: index]
        right_list = inorder[index + 1:]
        dfs(left_list, right_list, root, -2)
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
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution().buildTree(inorder, postorder)
    print_tree(root)
    # Solution().recoverTree(root)
    # print_tree(root)


if __name__ == '__main__':
    main()
