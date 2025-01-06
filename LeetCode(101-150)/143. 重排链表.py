# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        n = 0
        # 统计链表长度
        while p:
            p = p.next
            n += 1

        # 从中间拆分链表,前长后短
        i = 0
        p = head
        while i < n // 2:
            p = p.next
            i += 1
        q = p.next
        p.next = None

        # 逆置后半段链表
        r = ListNode(-1, None)
        while q:
            temp = q
            q = q.next
            temp.next = r.next
            r.next = temp
        r = r.next

        # 交叉链接链表
        p = head
        while p and r:
            temp_p = p.next
            temp_r = r.next
            p.next = r
            r.next = temp_p
            p = temp_p
            r = temp_r

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
    # head = [1,2,3,4]
    # head = [1,2,3,4,5]
    head = [1]
    head = create_linked_list(head)
    # print_linked_list(head)
    Solution().reorderList(head)
    print_linked_list(head)


if __name__ == '__main__':
    main()

        
