# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    def reverseBetween(self, head, left: int, right: int):
        dummy_node = ListNode(0,head)
        # find left
        left_prev, cur = dummy_node, head
        for _ in range(left-1):
            left_prev, cur = cur, cur.next  

        # reverse
        prev = None
        for _ in range(right-left+1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        # update pointers 
        left.next.next = cur
        left.next = prev

        return dummy_node.next
        
