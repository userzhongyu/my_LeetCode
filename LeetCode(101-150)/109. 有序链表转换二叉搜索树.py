# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        def dfs(_root: TreeNode, _left_list: list, _right_list: list):
            if len(_left_list) == 0:
                _root.left = None
                return
            else:
                _index = len(_left_list) // 2
                _root.left = _left_list[_index]
                dfs(_root.left, _left_list[: _index], _left_list[_index + 1:])
            if len(_right_list) == 0:
                _root.right = None
                return
            else:
                _index = len(_right_list) // 2
                _root.right = _right_list[_index]
                dfs(_root.right, _right_list[: _index], _right_list[_index + 1:])

        tree_list = []
        p = head
        while p:
            tree_list.append(TreeNode(p.val))
            p = p.next

        index = len(tree_list) // 2
        root = tree_list[index]
        left_list = tree_list[: index]
        right_list = tree_list[index + 1:]
        dfs(root, left_list, right_list)

        return root


# 将输入的形如“[1,2,3,4,5]”的字符串转换成链表
def create_ListNode():
    lst = list(input("list:")[1:-1].split(','))
    if lst == '[]':
        return ListNode()
    lst = [int(i) for i in lst]

    n = len(lst)

    # 头节点为空
    # head = ListNode()
    # tmp = ListNode(val=lst[0]
    # head.next = tmp

    # 头节点存数据
    head = tmp = ListNode(val=lst[0])
    for i in range(1, n):
        new = ListNode(val=lst[i])
        tmp.next = new
        tmp = tmp.next
    return head


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
    head = create_ListNode()
    root = Solution().sortedListToBST(head)
    print_tree(root)


if __name__ == '__main__':
    main()
