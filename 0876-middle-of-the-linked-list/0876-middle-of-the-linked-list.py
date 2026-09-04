# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        cu=head
        c=1
        while cu.next!=None:
            c+=1
            cu=cu.next
        
        for i in range(c//2):
            head=head.next
        
        return head
        

        