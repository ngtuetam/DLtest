class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head    # at the start of the linked list
        while last_node.next:
            last_node = last_node.next    # keep moving from node to node until get to the last of the LL
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head  # starting point

        # deleting head: update head to the next node
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # deleting node
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:   # key doesn't exist
            return 

        # cur_node.data = key
        prev_node.next = cur_node.next
        cur_node = None   # set the node to be deleted to None
    
    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return
        prev_node = None
        count = 0
        while cur_node and count != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node = None

    def length_iterative(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            # curr = curr.next       # curr.next = prev so this not right
            curr = tmp_next
        self.head = prev   # last node

    def merger_sorted_llist(self, l_list):
        p = self.head
        q = l_list.head
        s = None

        # handle the case if one of the linked lists is empty
        if not p:
            return q
        if not q:
            return p
        # if p and q is not None
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
        # the node with the lesser value will be the first node
        new_head = s
        # loop untill either p or q becomes None
        while p and q:
            if p.data <= q.data:
                s.next = p    # save what p is pointing to by assigning it to s.next
                s = p         # update the value of s to p because p.data is less than or equal to q.data
                p = s.next   # make p move along by pointing it to the next node of s
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head







# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# # llist.append("D")
# #
# # llist.prepend("0")
#
# # llist.insert_after_node(llist.head, "K")
#
# # llist.delete_node("B")
# # llist.delete_node("E")
#
# # print(llist.length_iterative())
#
# # print(llist.length_recursive(llist.head))
#
# # llist.swap_nodes("B", "C")
# llist.reverse_iterative()
# # llist.delete_node_at_pos(3)
# llist.print_list()

# llist_1 = LinkedList()
# llist_2 = LinkedList()
#
# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
#
# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)
#
# llist_1.merger_sorted_llist(llist_2)
# llist_1.print_list()