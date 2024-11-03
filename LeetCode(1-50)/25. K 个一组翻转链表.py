# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not self.enough(head, k):
            return head
        res_pre = ListNode(0)
        count = 0
        r = head
        # r指向第一个节点,需要后移k-1个节点
        while count < k - 1:
            r = r.next
            count += 1
        f, r = self.reverseList(head, r, k)
        # 设置头结点
        res_pre.next = f
        while self.enough(r.next, k):
            # 保存尾节点,用于钩链
            temp = r
            f = r.next
            count = 0
            # r指向每一个分组的头结点,需要后移k个节点
            while count < k:
                r = r.next
                count += 1
            f, r = self.reverseList(f, r, k)
            temp.next = f
        return res_pre.next

    # 剩余节点个数是否大于等于k个
    def enough(self, head: Optional[ListNode], k: int) -> bool:
        count = 0
        while head and count < k:
            head = head.next
            count += 1
        if count == k:
            return True
        else:
            return False

    # 逆置连续的k个节点,返回头结点和尾节点
    def reverseList(self, head: Optional[ListNode], rear: Optional[ListNode], k: int):
        """
        :param head: 头结点
        :param rear: 尾节点,保证链表连接
        :param k:
        :return: 头结点, 尾节点
        """
        # 头结点
        res_pre = ListNode(0)
        res_pre.next = rear.next
        p = head
        count = 0
        # 头插法逆置链表
        while count < k and p:
            q = p.next
            p.next = res_pre.next
            res_pre.next = p
            p = q
            count += 1
        return res_pre.next, head


def createLink():
    n = int(input('链表长度:'))
    val = 1
    head = ListNode(val)
    p = head
    for i in range(1, n):
        # val = int(input())
        q = ListNode(i + 1)
        p.next = q
        p = q
    p.next = None
    return head


def show(head: ListNode):
    while head.next:
        print(head.val, end='->')
        head = head.next
    print(head.val)


def main():
    ob = Solution()
    head = createLink()
    show(head)
    k = int(input('k值:'))
    res = ob.reverseKGroup(head, k)
    show(res)


if __name__ == '__main__':
    main()