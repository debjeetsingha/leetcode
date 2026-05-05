"""
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two Pass Solution

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur1 = head
        no_of_node = 0
        
        while cur1:
            no_of_node+=1
            cur1=cur1.next
        if no_of_node==1:
            return None

        to_move = no_of_node - n
        dummy = ListNode(next=head)
        cur2 = dummy
        for x in range(to_move):
            cur2 = cur2.next
        
        cur2.next = cur2.next.next
        return dummy.next
