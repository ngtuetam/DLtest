# Definition for singly-linked list.
# O(m+n)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def getlength(self,head):
        list_length = 0
        while head:
            head = head.next
            list_length += 1
        return list_length

    def getIntersectionNode(self, head1: ListNode, head2: ListNode):
        list1_len = self.getlength(head1)
        list2_len = self.getlength(head2)
        list1_node = ListNode()
        list2_node = ListNode()

        length_diff = 0

        if list1_len >= list2_len:
            length_diff = list1_len - list2_len
            list1_node = head1
            list2_node = head2
        else:
            length_diff = list2_len - list1_len
            list1_node = head2
            list2_node = head1

        while length_diff > 0:
            list1_node = list1_node.next
            length_diff -=1
        
        while list1_node:
            if list1_node == list2_node:
                return list1_node
            
            list1_node = list1_node.next
            list2_node = list2_node.next
        return None

            


    


