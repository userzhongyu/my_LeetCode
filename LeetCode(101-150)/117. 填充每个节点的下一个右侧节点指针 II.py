# Definition for a Node.
from typing import Optional
import math


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 当 root == None时，没有 next 指针，报错 AttributeError: 'NoneType' object has no attribute 'left'
        if not root:
            return None
        cur = root
        cur.next = None
        while cur:
            # 创建链表2
            head = tail = Node()
            while cur:
                # 构建链表2
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            # 处理每一层最后一个节点
            tail.next = None
            # 链表1 指向下一层的第一个节点
            cur = head.next
        return root


# 层序遍历构建二叉树
def build_tree_from_level_order(level_order):
    # if not level_order:
    #     return None

    root = Node(level_order[0])  # 创建根节点
    queue = [root]
    index = 1

    while index < len(level_order):
        node = queue.pop(0)  # 取出当前节点
        if level_order[index] is not None:  # 如果左子节点存在
            node.left = Node(level_order[index])
            queue.append(node.left)
        index += 1

        if index < len(level_order) and level_order[index] is not None:  # 如果右子节点存在
            node.right = Node(level_order[index])
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
    root = [1, 2, 3, 4, 5, None, 7]
    # root = []
    root = build_tree_from_level_order(root)
    print(Solution().connect(root))


if __name__ == '__main__':
    main()
