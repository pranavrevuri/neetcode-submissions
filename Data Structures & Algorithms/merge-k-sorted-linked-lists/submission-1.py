# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, head1, head2):
            res = ListNode()
            cur = res

            h1 = head1
            h2 = head2

            while h1 and h2:
                if h1.val >= h2.val:
                    cur.next = h2
                    h2 = h2.next
                    cur = cur.next
                else:
                    cur.next = h1
                    h1 = h1.next
                    cur = cur.next
            
            cur.next = h1 if h1 else h2
            
            return res.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        for i in range(1, len(lists)):
            lists[i] = self.merge2Lists(lists[i], lists[i - 1])
        
        return lists[-1]
