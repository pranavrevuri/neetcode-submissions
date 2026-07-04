# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def reverseLL(self, head):
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
   
   
   
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.findMiddle(head)
        sec = mid.next
        mid.next = None

        first = head
        rev = self.reverseLL(sec)

        while rev:
            temp_rev = rev.next
            temp_first = first.next
            rev.next = temp_first

            first.next = rev
            
            rev = temp_rev
            first = temp_first









