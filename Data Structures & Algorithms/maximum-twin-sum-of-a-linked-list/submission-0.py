# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        nums = []
        while fast and fast.next:
            nums.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        res = 0
        for i in nums[::-1]:
            res = max(res, i+slow.val)
            slow = slow.next
        return res
        