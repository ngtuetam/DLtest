# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        first = head
        second = head

        for i in range(n):
            if second.next is None:
                if i == n-1:
                    head = head.next
                return head
            second = second.next

        while second.next:
            second = second.next
            first = first.next

        first.next = first.next.next

        return head


    