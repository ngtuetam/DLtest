# leetcode
# Given the head of a linked list, rotate the list to the right by k places.
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# connect tail with head, then disconnect new tail with new head

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
        
    def rotate_right(self, k):
        if self.head is None:
            return None
        
        # connect tail to head
        cur = self.head
        length = 1
        while cur.next:
            cur = cur.next
            length +=1
        # cur now point to tail
        cur.next = self.head

        # move to new head
        k = length - (k%length)
        while k >0:
            cur = cur.next
            k-=1
        # cur now point to the previous of new head
        self.head = cur.next
        cur.next = None
        return self.head






my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.insert(6)
my_list.rotate_right(2)
my_list.print_list()