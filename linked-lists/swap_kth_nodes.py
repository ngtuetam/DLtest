# leetcode: Swapping Nodes in a Linked List
# Input: head = [1,2,3,4,5], k = 2
#  Output: [1,4,3,2,5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head, k: int):
        t = head
        n = 0
        while t:
            n += 1
            t = t.next

        
        # edge case 
        if n < k:
            return None
        if 2*k - 1 == n:
            return head

        
        # find x and previous of k-th node
        x = head
        x_prev = ListNode(None)
        for _ in range(k-1):
            x_prev = x 
            x = x.next

        # kth node from end is (n-k + 1)th node from beginning 
        y = head
        y_prev = ListNode(None)
        for _ in range(n-k):
            y_prev = y
            y = y.next

        if x_prev is not None:
            x_prev.next = y

        if y_prev is not None:
            y_prev.next = x

        temp = x.next
        x.next = y.next
        y.next = temp
  
        # Change head pointers when k is 1 or n
        if k == 1:
            head = y
  
        if k == n:
            head = x

        return head