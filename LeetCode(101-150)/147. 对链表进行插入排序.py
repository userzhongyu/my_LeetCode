# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        q = p.next
        p.next = None
        while q:
            cur = q
            q = q.next
            # 取所需插入位置的前一个节点的指针
            loc = ListNode(-1, p)
            # 寻找插入位置
            while loc.next and loc.next.val <= cur.val:
                loc = loc.next
            # 插入索引为0的位置，单独处理
            if loc.next == p:
                loc.next = cur
                cur.next = p
                p = cur
            # 插入其他位置
            else:
                temp = loc.next
                loc.next = cur
                cur.next = temp
        head = p
        return head





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
    # head = [-1,5,3,4,0]
    # head = [2,1]
    head = [1]
    head = create_linked_list(head)
    print_linked_list(head)
    head = Solution().insertionSortList(head)
    print_linked_list(head)


if __name__ == '__main__':
    main()

        
