# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        cu=dummy
        while cu.next!=None:
            if cu.next.val==val:
                cu.next=cu.next.next
            else:
                cu=cu.next
        
        return dummy.next
        