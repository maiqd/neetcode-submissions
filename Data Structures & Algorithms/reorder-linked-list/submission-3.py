# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow is middle
        curr = slow.next
        slow.next = pre = None
        # reverse 2nd list
        while curr:
            tmp_nxt = curr.next
            curr.next = pre
            pre = curr
            curr = tmp_nxt

        first, second = head, pre
        # merge 2 list
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first, second = tmp1, tmp2
