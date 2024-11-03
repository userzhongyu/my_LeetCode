"""
@Time ： 2024/7/17 下午10:25
@Auth ： user_zhong
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_ListNode(self, l: list):
        n = len(l)
        head = tmp = ListNode(val=l[0])
        for i in range(1, n):
            new = ListNode(val=l[i])
            tmp.next = new
            tmp = tmp.next
        return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ans = ListNode(next=head)
        while pre.next and pre.next.next:
            val = pre.next.val  # 保存现场

            # 重复则删除节点
            if pre.next.next.val == val:
                while pre.next.next and pre.next.next.val == val:
                    pre.next = pre.next.next
                pre.next = pre.next.next
            # 不重复则后移指针
            else:
                pre = pre.next

        return ans.next if ans else ans


def main():
    print("input:")
    l = list(input())
    print("list:", l)
    head = ListNode().create_ListNode(l)
    ans = Solution().deleteDuplicates(head)
    while ans:
        print(ans.val,end='')
        ans = ans.next


if __name__ == '__main__':
    main()
