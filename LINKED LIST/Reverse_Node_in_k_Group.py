# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        temp=head
        count=0

        while count < k :
            if temp is None:
                return head
            
            temp=temp.next
            count+=1
        
        prevnode = self.reverseKGroup(temp,k)
        temp = head
        cnt = 0

        while cnt<k:
            nxt = temp.next
            temp.next = prevnode
            prevnode=temp
            temp=nxt
            cnt+=1

        return prevnode
