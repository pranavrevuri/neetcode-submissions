# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        
        prev = ListNode()
        it = prev

        while cur:
            if cur.val != val: 
                temp = cur.next
                it.next = cur
                it = it.next
                cur = temp
            else:
                cur = cur.next
        
        it.next = None
        return prev.next