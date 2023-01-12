class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_llist(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
def merge_list(head_a, head_b):

    # add dummy node to store the result
    dummy_node = Node(0)

    # tail store the last node
    tail = dummy_node


    while True:
        if head_a is None:
            tail.next = head_b
            break
        if head_b is None:
            tail.next = head_a
            break
        
        if head_a.value <= head_b.value:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next
        
        # update tail
        tail = tail.next

    return dummy_node.next


llist_a = LinkedList(5)
llist_b = LinkedList(2)


llist_a.append(10)
llist_a.append(15)


llist_b.append(3)
llist_b.append(20)

# llist_a.head = merge_list(llist_a.head, llist_b.head)
# llist_a.print_llist()

print(llist_a.head.value)