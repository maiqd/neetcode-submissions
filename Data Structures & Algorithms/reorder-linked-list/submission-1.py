# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid is slow

        # reverse 2nd list
        second_head = slow.next
        slow.next = None

        pre = None
        curr = second_head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next

        # merge 2 list
        first = head
        second_head = pre
        while second_head:
            tmp1, tmp2 = first.next, second_head.next

            first.next = second_head
            second_head.next = tmp1

            first = tmp1
            second_head = tmp2
