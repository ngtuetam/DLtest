# Remove duplicates from an unsorted linked list
# Using hashmap, O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
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
        new_node = ListNode(value)
        if (self.head):
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node

    def delete_duplicate(self):

        # base case
        if self.head == None or self.head.next == None:
            return self.head

        # create a hash to store seen value
        hashmap = set()

        cur = self.head
        hashmap.add(self.head.value)
        while cur.next:
            if cur.next.value in hashmap:
                cur.next = cur.next.next
            else:
                hashmap.add(cur.next.value)
                cur = cur.next

        return self.head

        
        

my_list = LinkedList()
my_list.insert(4)
my_list.insert(89)
my_list.insert(89)
my_list.insert(10)
my_list.insert(3)
my_list.insert(89)
my_list.insert(89)
my_list.insert(10)
my_list.insert(10)
my_list.delete_duplicate()
my_list.print_list()

