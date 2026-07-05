# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            return None
        
        first = head
        second = head

        for i in range(n):
            first = first.next

        if first == None:
                temp = second.next
                second.next = None
                second = temp
                return second

        while first:
            if first.next == None:
                second.next = second.next.next
            
            first = first.next
            second = second.next
        
        return head
        
        

        