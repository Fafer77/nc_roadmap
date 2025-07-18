from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        ll_len = 0
        curr = head
        while curr:
            ll_len += 1
            curr = curr.next

        to_delete_idx = ll_len - n
        if to_delete_idx == 0:
            return head.next

        prev = None
        curr = head

        while to_delete_idx != 0:
            prev = curr
            curr = curr.next
            to_delete_idx -= 1

        prev.next = curr.next
        curr.next = None

        return head
