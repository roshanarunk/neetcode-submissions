# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)

        fast = head

        while fast and n != 0:
            fast = fast.next
            n = n-1
        
        prev = dummy
        while head and fast:
            prev = prev.next
            head = head.next
            fast = fast.next
        prev.next = prev.next.next
        
        print(head.val)

        return dummy.next