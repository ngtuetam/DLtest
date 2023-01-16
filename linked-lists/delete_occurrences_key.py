# Delete all occurrences of a given key in a linked list
# Given the head of a linked list and a key, delete all nodes whose values match the given key.
# Input: 2 -> 2 -> 1 -> 8 -> 2 ->  3 -> 2 -> 7
#        Key to delete = 2
# Output:  1 -> 8 -> 3 -> 7 

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

    def delete_occurrences(self,key):
        dummy_node = Node()
        dummy_node.next = self.head

        cur = dummy_node
        while cur.next:
            if cur.next.value == key:
                cur.next = cur.next.next
            else:
                cur = cur.next
        self.head = dummy_node.next
        return dummy_node



my_list = LinkedList()
my_list.insert(89)
my_list.insert(89)
my_list.insert(10)
my_list.insert(3)
my_list.insert(89)
my_list.insert(89)
my_list.insert(10)
my_list.insert(10)
my_list.delete_occurrences(89)
my_list.print_list()


