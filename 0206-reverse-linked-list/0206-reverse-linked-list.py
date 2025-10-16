# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        #when curr is none our prev will stuck on the head of our new list
        while curr != None:
            #store next for later curr
            ourNext = curr.next

            #point to previous node
            curr.next = prev

            #establish current node as new previous
            prev = curr

            #make curr our stored node
            curr = ourNext
        
        
        return prev

            
        