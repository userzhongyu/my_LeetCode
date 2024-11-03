"""
@Time ： 2024/7/26 下午8:23
@Auth ： user_zhong
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_ListNode(self):
        l = input("input:")
        if l == '[]':
            return ListNode()
        l = l[1: -1]
        l = l.split(',')
        n = len(l)
        head = tmp = ListNode(val=int(l[0]))
        for i in range(1, n):
            new = ListNode(val=int(l[i]))
            tmp.next = new
            tmp = tmp.next
        return head


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ans = ListNode()
        p = ListNode(next=head)
        q = ans
        flag = True
        while p.next:
            if p.next.val < x:
                q.next = p.next
                q = q.next
                p.next = p.next.next
            elif flag:
                r = p.next
                p = p.next
                flag = False
            else:
                p = p.next
        if not flag:
            q.next = r
        return ans.next


def main():
    head = ListNode().create_ListNode()
    x = int(input("x:"))
    ans = Solution().partition(head, x)
    while ans:
        print(ans.val, end='')
        ans = ans.next


if __name__ == '__main__':
    main()
