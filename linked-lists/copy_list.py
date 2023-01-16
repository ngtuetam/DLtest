# leetcode: Copy List with Random Pointer

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a hash map, init None -> None for edge case
        oldtocopy = {None:None}
        # first pass to init value
        cur = head
        while cur:
            copy_node = Node(cur.val)
            oldtocopy[cur] = copy_node
            cur = cur.next
        # second pass to connecting
        cur = head
        while cur:
            copy_node = oldtocopy[cur]
            copy_node.next = oldtocopy[cur.next]
            copy_node.random = oldtocopy[cur.random]
            cur = cur.next
        return oldtocopy[head]
