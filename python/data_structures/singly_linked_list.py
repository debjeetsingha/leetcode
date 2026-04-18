"""
In a singly linked list, each Node has two attributes:
    value: stores a vale
    next: points to the next Node

In the last Node, next points to nothing.

When making a Linked List, start with dummy node and remove it in the end.
"""


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

node1 = ListNode(5)
node2 = ListNode(10)
node3 = ListNode(20)
node4 = ListNode(15)

node1.next = node2
node2.next = node3
node3.next = node4

def traverseList(head):
    cur = head
    while cur:
        print(cur.val, end=' -> ')
        cur = cur.next
    print('done')

traverseList(node1)

    
