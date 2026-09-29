# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        head = l1
        while l1 and l2:
            sum = l1.val + l2.val + carry 
            if sum >= 10:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            l1.val = sum
            if not l1.next:
                l1.next = l2.next
                l2.next = None
            prev = l1
            l1 = l1.next
            l2 = l2.next
        while carry:
            if l1:
                sum = l1.val + carry
                if sum >= 10:
                    carry = 1
                    sum = sum - 10
                else:
                    carry = 0
                l1.val = sum
                prev = l1
                l1 = l1.next
            else:
                prev.next = ListNode(1, None)
                carry = 0




        return head
    
        