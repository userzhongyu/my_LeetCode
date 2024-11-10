# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        # 增加一个空的头节点
        tmp = ListNode(next=head)
        head = tmp
        p = head
        if p.next:
            q = p.next
        # 移动到第left-1个节点
        for i in range(left-1):
            p = q
            q = q.next

        # 头插法实现反转
        for i in range(right-left):
            r = q.next
            q.next = r.next
            r.next = p.next
            p.next = r
        return head.next

    def create_ListNode(self):
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


def main():
    head = Solution().create_ListNode()
    left = int(input("left:"))
    right = int(input("right:"))
    head = Solution().reverseBetween(head, left, right)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
