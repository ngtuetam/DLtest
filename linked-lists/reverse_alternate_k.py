# Reverse alternate K nodes in a Singly Linked List
# Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.
# Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
# Output:   3->2->1->4->5->6->9->8->7->NULL. 
# https://www.geeksforgeeks.org/reverse-alternate-k-nodes-in-a-singly-linked-list-iterative-solution/?ref=rp
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
    def kAltReverse(self, k):
        
        prev = None
        curr = self.head
        temp = None
        tail = None
        newHead = None
        join = None
        t = 0
    
        # Traverse till the end of the linked list
        while (curr != None) :
        
            t = k
            join = curr
            prev = None
    
            # Reverse alternative group of k nodes
            # of the given linked list
            while (curr != None and t > 0):
                
                t = t - 1
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Sets the new head of the input list
            if (newHead == None):
                newHead = prev
    
            # Tail pointer keeps track of the last node
            # of the k-reversed linked list. The tail pointer
            # is then joined with the first node of the
            # next k-nodes of the linked list
            if (tail != None):
                tail.next = prev
    
            tail = join
            tail.next = curr
    
            t = k
    
            # Traverse through the next k nodes
            # which will not be reversed
            while (curr != None and t > 0):
                t = t - 1
                prev = curr
                curr = curr.next
            
            # Tail pointer keeps track of the last
            # node of the k nodes traversed above
            tail = prev
        
        # newHead is new head of the modified list
        # return newHead
        self.head = newHead
        return self.head


my_list = LinkedList()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.insert(6)
print(my_list.kAltReverse(3))
my_list.print_list()

