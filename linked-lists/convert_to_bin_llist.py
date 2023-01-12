# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        tmp = head
        while tmp:
            l.append(tmp.val)
            tmp = tmp.next
        l = [str(i) for i in l] 
        num = str("".join(l))
        bin = int(num,2)
        return bin
        