# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode(-1)
        cur3 = dummy
        carry = 0
        digit = 0
        while cur1 or cur2:
            if (cur1==None) and (cur2!=None):
                    total = cur2.val + carry
                    cur2 = cur2.next
            elif (cur2==None) and (cur1!=None):
                    total = cur1.val + carry
                    cur1 = cur1.next
            elif cur1 and cur2:
                total = cur1.val + cur2.val + carry
                cur1 = cur1.next
                cur2 = cur2.next
            

            digit = total% 10
            carry = total// 10

            
            new_node = ListNode(digit)
            cur3.next = new_node
            cur3 = cur3.next

        if carry==1:
            new_node = ListNode(carry)
            cur3.next = new_node

        return dummy.next