# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        first =head
        sec=head.next
        prev=None
        if first is not None and sec.next is not None:
            third=sec.next
            sec.next=first
            first.next=third
            if prev is not None:
                prev.next=sec
            else:
                head=sec
            prev = first
            first = third
            if third is not None:
                sec = third.next
            else:
                head=sec
