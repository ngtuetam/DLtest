# leetcode : Insertion Sort List
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        dummy_node = ListNode()
        cur = head

        while cur:
            prev = dummy_node

            while prev.next and prev.next.val <= cur.val:
                prev = prev.next
            
            next = cur.next
            cur.next = prev.next
            prev.next = cur

            cur = next
        return dummy_node.next