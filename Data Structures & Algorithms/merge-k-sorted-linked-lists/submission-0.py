# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        FullList = []
        
        for head in lists:
            node = head
            while node:                
                FullList.append(node.val)
                node = node.next


        if not FullList:
            return None

        FullList.sort()

        head = ListNode(val = FullList[0])
        node = head
        for val in FullList[1:]:
            node.next = ListNode(val)
            node = node.next

        return head
