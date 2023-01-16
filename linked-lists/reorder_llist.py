# L0 → L1 → … → Ln - 1 → Ln
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# O(n^2) approach
# 1) Initialize current node as head.
# 2) While next of current node is not null, do following
#     a) Find the last node, remove it from the end and insert it as next
#        of the current node.
#     b) Move current to next to next of current
# https://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/
class Node:
    def __init__(self,value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while(cur):
            print(cur.value)
            cur = cur.next
    
    def insert(self,value):
        new_node = Node(value)
        if (self.head):
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node
    
    def length(self):
        cur = self.head
        cnt = 0
        while cur:
            cnt +=1
            cur = cur.next
        return cnt
    def reverselist(self, head):
        prev = None
        curr = head
        next=None
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
    def reorder_list(self):
        #find the middle point using tortoise and hare method
        slow = self.head
        fast = slow.next
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        # split the linked list in two halves
        # node1, head of first half    1 -> 2 -> 3
        # node2, head of second half   4 -> 5 -> 6
        node1 = self.head
        node2 = slow.next
        slow.next = None
        # reverse half second
        prev = None
        curr = node2
        next=None
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        node2 = prev
        #  Merge alternate nodes
        node = Node(0)  #Assign dummy Node
        
        # curr is the pointer to this dummy Node, which
        # will be used to form the new list
        curr = node
        
        while (node1 != None or node2 != None):
            
            # First add the element from first list
            if (node1 != None):
                curr.next = node1
                curr = curr.next
                node1 = node1.next
            
            # Then add the element from second list
            if(node2 != None):
                curr.next = node2
                curr = curr.next
                node2 = node2.next
        
        # Assign the head of the new list to head pointer
        node = node.next
        return self.head



my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.insert(6)
my_list.reorder_list()
my_list.print_list()
