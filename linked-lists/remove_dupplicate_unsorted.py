# Remove duplicates from an unsorted linked list
# O(N^2)

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
        if self.head == None:
            return None
        pt1 = self.head
        while pt1 and pt1.next:
            pt2 = pt1
            while pt2.next:
                if pt1.value == pt2.next.value:
                    remove = pt2.next
                    pt2.next = pt2.next.next
                    remove = None
                else:
                    pt2 = pt2.next
            pt1 = pt1.next
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

