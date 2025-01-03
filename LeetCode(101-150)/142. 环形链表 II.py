# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 第一次相遇(实际上为第二次,初始化 slow 和 fast 时已经相遇过一次)
            if fast == slow:
                fast = head
                # 再次移动指针
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return fast
        # 不存在环
        return None


# 将输入的形如“[1,2,3,4,5]”的字符串转换成链表
def createLinkedListWithCycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def main():
    # head = [3, 2, 0, -4]
    # pos = 1
    head = [1, 2]
    pos = 0
    # head = [1]
    # pos = -1
    head = createLinkedListWithCycle(head, pos)
    temp = Solution().detectCycle(head)
    if temp:
        print(temp.val)
    else:
        print(temp)


if __name__ == '__main__':
    main()
