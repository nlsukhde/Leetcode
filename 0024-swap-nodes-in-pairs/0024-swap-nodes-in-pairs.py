# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        if head == None:
            return None
        elif head.next == None:
            return head
        else: #swapping every 2 so we do next.next?
           first = head
           second = head.next

           tail = self.swapPairs(head.next.next)

           second.next = first
           first.next = tail


           return second

        