# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        # 找到链表中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # 递归
        left = self.sortList(head)
        right = self.sortList(mid)

        # 将 left 和 right 合并
        res = cur = ListNode()
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        # 处理尾部
        if left:
            cur.next = left
        else:
            cur.next = right

        return res.next


def create_linked_list(values):
    """
    从列表创建链表
    :param values: List[int] 输入值列表
    :return: ListNode 链表头节点
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    """
    打印链表
    :param head: ListNode 链表头节点
    """
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))


def main():
    head = [4, 2, 1, 3]
    # head = [1]
    # head = [5, 4, 3, 2, 1]
    # head = []
    head = create_linked_list(head)
    res = Solution().sortList(head)
    print_linked_list(res)


if __name__ == '__main__':
    main()
