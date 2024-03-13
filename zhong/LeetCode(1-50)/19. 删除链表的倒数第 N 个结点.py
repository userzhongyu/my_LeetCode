"""
双指针,间隔n,同时移动
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        count = 1
        i = ListNode()
        # i的后继节点为需要删除的节点
        i.next = head
        j = head
        while j.next and count < n:
            j = j.next
            count += 1
        while j.next:
            i = i.next
            j = j.next
        if i.next == head:
            head = head.next
        else:
            i.next = i.next.next
        return head