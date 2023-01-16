# leetcode: Sort List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        # base case
        if head is None or head.next is None:
            return head
        mid = self.getmid(head)
        new_head_1 = self.sortList(head)
        new_head_2 = self.sortList(mid)
        final_head = self.merge(new_head_1,new_head_2)
        return final_head

    def getmid(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    

    def merge(self,list1, list2):
        # dummy_node of the result linked list
        dummy_node = ListNode(0)
        tail = dummy_node

        while True:
            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # update tail
            tail = tail.next
        # return head of the result linked list
        return dummy_node.next
            
