# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        left, right = head, head.next
        while right:
            gcd = ListNode(math.gcd(left.val, right.val))
            gcd.next = right
            left.next = gcd
            left = right
            right = right.next
        return head