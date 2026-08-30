# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        c=dummy
        ca=0

        while l1 or l2 or ca:
            if l1:
                a=l1.val
            else:
                a=0

            if l2:
                b=l2.val
            else:
                b=0

            tot=a+b+ca
            di=tot%10
            ca=tot//10
            c.next=ListNode(di)
            c=c.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return dummy.next

        