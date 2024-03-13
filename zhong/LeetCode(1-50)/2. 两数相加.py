# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2 :
            return l1
        rlst = ListNode()
        head = rlst
        temp = 0
        c = 0
        while l1 != None or l2 != None or c != 0:
            if l1 != None and l2 != None:
                temp= l1.val + l2.val + c
                l1 = l1.next
                l2 = l2.next
            elif l1 != None:
                temp = l1.val + c
                l1 = l1.next
            elif l2 != None:
                temp = l2.val + c
                l2 = l2.next
            elif c != 0:
                temp = c
            if temp >= 10:
                c = 1
                temp = temp % 10
            else:
                c = 0
            rlst.next = ListNode(temp)
            rlst = rlst.next
        rlst.next = None

        return  head.next

def main():
    l = ListNode()
    l1 = l
    for i in [9,9,9,9,9,9,9]:
        temp = ListNode()
        temp.val = i
        l. next = temp
        l = l.next
    l1 = l1.next
    l = ListNode()
    l2 = l
    for i in [9,9,9,9]:
        temp = ListNode()
        temp.val = i
        l.next = temp
        l = l.next
    l2 = l2.next
    sol = Solution()
    rlst = sol.addTwoNumbers(l1,l2)
    temp = rlst
    while temp != None:
        print(temp.val,end=" ")
        temp = temp.next

if __name__ == '__main__':
    main()
