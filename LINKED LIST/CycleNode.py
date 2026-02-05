# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def CycleNode(self, head):
        slow = fast = head
        isCycle = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                isCycle = True
                break
            
        if not isCycle:
            return None

        slow = head
        while fast is not slow:
            slow = slow.next
            fast = fast.next
                   
        return slow
