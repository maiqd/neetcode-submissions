# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # find the mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is the mid, now revese the linked list start from slow

        second = slow.next
        pre = None
        slow.next = None
        while second:
            next = second.next
            second.next = pre
            pre = second
            second = next

        first, second = head, pre
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
