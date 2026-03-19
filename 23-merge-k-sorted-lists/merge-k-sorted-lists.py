# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Step 1: Push first node of each list into heap
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        
        # Step 2: Create dummy node
        dummy = ListNode(0)
        curr = dummy

        # Step 3: Process heap
        while heap:
            val, i, node = heapq.heappop(heap)
            
            curr.next = node
            curr = curr.next

            # If next node exists, push into heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next