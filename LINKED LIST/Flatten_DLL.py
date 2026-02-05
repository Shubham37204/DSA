# Definition for Doubly-linked list.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        if head is None:
            return head
        
        curr = head
        while curr is not None:
            if curr.child is not None:
                nxt = curr.next  # avoid using 'next' as it's a built-in
                child = self.flatten(curr.child)  
                curr.next = child
                child.prev = curr
                curr.child = None

                while curr.next is not None:
                    curr = curr.next

                if nxt is not None:
                    curr.next = nxt
                    nxt.prev = curr  

            curr = curr.next  
        
        return head  
