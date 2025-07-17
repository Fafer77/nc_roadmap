from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr_first = list1
        curr_snd = list2

        dummy_head = ListNode()
        curr = dummy_head

        while curr_first and curr_snd:
            if curr_first.val < curr_snd.val:
                curr.next = curr_first
                curr = curr_first
                curr_first = curr_first.next
            else:
                curr.next = curr_snd
                curr = curr_snd
                curr_snd = curr_snd.next
            
        while curr_first:
            curr.next = curr_first
            curr = curr_first
            curr_first = curr_first.next
        
        while curr_snd:
            curr.next = curr_snd
            curr = curr_snd
            curr_snd = curr_snd.next

        return dummy_head.next
