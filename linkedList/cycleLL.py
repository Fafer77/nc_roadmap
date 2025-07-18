from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow_ptr = head
        fast_ptr = head

        while fast_ptr != None and slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if fast_ptr == None:
            return False
        else:
            return True
        

sol = Solution()
print(sol.hasCycle([1,2]))
