# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        a=list1
        b=list2
        dummy=ListNode(0)
        c=dummy

        while a and b:
            if a.val<=b.val:
                c.next=a
                a=a.next
            else:
                c.next=b
                b=b.next

            c=c.next

        if a:
            c.next=a
        elif b:
            c.next=b

        return dummy.next
        