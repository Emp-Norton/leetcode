from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_merged_list = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                new_merged_list.val=list1.pop().val
            else:
                new_merged_list.val=list2.pop().val
