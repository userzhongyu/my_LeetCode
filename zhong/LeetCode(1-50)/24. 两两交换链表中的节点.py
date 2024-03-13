# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode(0)
        p.next = head
        res_pre = p
        # 依次两两交换
        while p.next and p.next.next:
            temp = p.next.next
            p.next.next = temp.next
            temp.next = p.next
            p.next = temp
            p = p.next.next
        return res_pre.next
