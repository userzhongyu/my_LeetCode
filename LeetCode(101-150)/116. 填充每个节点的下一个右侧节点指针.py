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
        # 当 root == None时，len(queue) == 1，报错 AttributeError: 'NoneType' object has no attribute 'left'
        if not root:
            return None
        queue = [root]
        i = 0
        # 层序遍历
        while i < len(queue):
            node = queue[i]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 1

        # 按照高度进行分区
        h = int(math.log2(len(queue) + 1))
        for i in range(h):
            for j in range(2 ** i):
                # 判断是否为本层最后一个节点
                if j + 1 < 2 ** i:
                    queue[j + 2 ** i - 1].next = queue[j + 2 ** i - 1 + 1]
                else:
                    queue[j + 2 ** i - 1].next = None

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
    # root = [1, 2, 3, 4, 5, 6, 7]
    root = []
    # root = build_tree_from_level_order(root)
    print(Solution().connect(None))


if __name__ == '__main__':
    main()
