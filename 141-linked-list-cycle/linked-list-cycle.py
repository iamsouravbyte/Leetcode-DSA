# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # slow moves 1 step at a time
        # fast moves 2 steps at a time
        slow = head
        fast = head

        # Traverse the list
        # We need to check fast and fast.next because fast moves 2 steps
        while fast is not None and fast.next is not None:
            
            # Move slow by 1 step
            slow = slow.next
            
            # Move fast by 2 steps
            fast = fast.next.next

            # If there is a cycle, fast and slow will meet at some point
            if fast == slow:
                return True
        
        # If fast reaches the end (null), no cycle exists
        return False