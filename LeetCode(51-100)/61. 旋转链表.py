from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        h = head
        while h:
            n += 1
            h = h.next
        if n == 0:
            return head
        count = 0
        k = k % n
        if k == 0:
            return head
        h1, end1 = head, head
        while count < n - k - 1:
            end1 = end1.next
            count += 1
        if end1.next:
            h2, end2 = end1.next, end1.next
            while end2.next:
                end2 = end2.next
            end1.next = None
            end2.next = h1
            return h2
        else:
            return h1


def main():
    lst = eval(input())
    k = eval(input())
    head = ListNode()
    p = head
    for i in lst:
        q = ListNode(i, None)
        p.next = q
        p = q
    head = head.next
    head = Solution().rotateRight(head, k)
    while head:
        print(head.val, end='->')
        head = head.next


if __name__ == '__main__':
    main()
