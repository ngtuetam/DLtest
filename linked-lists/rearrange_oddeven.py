# Rearrange a linked list such that all even and odd positioned nodes are together
# Input:   1->2->3->4
# Output:  1->3->2->4

# Input:   10->22->30->43->56->70
# Output:  10->30->56->22->43->70

# connect odd nodes and even nodes, keep 1 even head
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

    def reverse_oddeven(self):
        if self.head == None:
            return None
        
        # init odd and even
        odd = self.head
        even = odd.next

        even_head = even
        while True:
            if odd == None or even == None or even.next == None:
                odd.next = even_head
                break

            # Connecting odd nodes 
            odd.next = even.next
            odd = even.next

            # if no more even node after current odd (size = odd)
            if odd.next == None:
                even.next = None
                odd.next = even_head
                break

            # connecting even nodes
            even.next = odd.next
            even = odd.next

        return self.head



my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.insert(6)
my_list.insert(7)
my_list.reverse_oddeven()
my_list.print_list()

