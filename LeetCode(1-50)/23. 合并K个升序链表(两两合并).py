"""
逐个加入已有序的链表
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        while True:
            temp = []
            # 链表个数为奇数时,加入一个空链表
            if len(lists) % 2 != 0:
                lists.append(None)
            for i in range(0, len(lists) - 1, 2):
                temp.append(self.mergeTwo(lists[i], lists[i + 1]))
            lists = temp
            # 一次合并后新链表的长度
            if len(lists) == 1:
                break
        return lists[0]

    def mergeTwo(self, l1: ListNode, l2: ListNode):
        res = ListNode(0, None)
        temp = res
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return res.next
