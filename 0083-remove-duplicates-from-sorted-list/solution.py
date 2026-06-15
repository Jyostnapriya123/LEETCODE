# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        ptr=head
        while ptr!=None and ptr.next!=None:
            if ptr.val==ptr.next.val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head     
