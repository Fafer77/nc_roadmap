from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (head is None) or (head.next is None) or (head.next.next is None):
            return
        
        slow_ptr = head
        fast_ptr = head

        # find middle of linked list
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # split list and reverse second half
        snd_list = slow_ptr.next
        slow_ptr.next = None

        new_snd_ll_head = None
        curr = snd_list

        while curr:
            next_node = curr.next
            curr.next = new_snd_ll_head
            new_snd_ll_head = curr
            curr = next_node
        
        first_ll_head = head
        while first_ll_head and new_snd_ll_head:
            new_first = first_ll_head.next
            new_second = new_snd_ll_head.next
            first_ll_head.next = new_snd_ll_head
            new_snd_ll_head.next = new_first
            first_ll_head = new_first
            new_snd_ll_head = new_second
