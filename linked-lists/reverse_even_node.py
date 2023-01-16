# Reverse Even Nodes in a Linked List
# Given a singly linked list, reverse the nodes at even positions.
# Input: A[] = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
# Output: 1 6 3 4 5 2
# maintain 2 linked list, then merge

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

    def reverse_even(self):
        even = None
        odd = self.head
        if odd == None or odd.next == None or odd.next.next == None:
            return None
        while odd and odd.next:

            # store even node in tmp
            tmp = odd.next
            odd.next = tmp.next
            # add even node to even list
            tmp.next = even
            # move even to head of list
            even = tmp
            # update odd
            odd = odd.next

        odd = self.head

        # now we have 2 lists, odd and even, odd is head of odd list and even is head of even list

        while even:
            # store tmp to even next, keep connecting
            tmp = even.next
            # connect odd list to even list
            even.next = odd.next
            odd.next = even

            # update even to the next element in even list
            even = tmp
            # update odd
            odd = odd.next.next

        return self.head




my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.insert(6)
my_list.reverse_even()
my_list.print_list()

