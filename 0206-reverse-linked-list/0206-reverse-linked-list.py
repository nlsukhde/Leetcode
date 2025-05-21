# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next #store curr next so we have it
            curr.next = prev #point to previous node(default none in the first node)
            prev = curr #store current as prev so we have it for the next node
            curr = next #set current as stored next
        
        return prev

