class Solution(object):
    def swap_head(self,head,N):
        swap_node = head
        while N>1:
            if not swap_node:
                return None
            swap_node = swap_node.next
            N-=1
        if swap_node.next:
            after_swap_node = swap_node.next.next
            after_head = head.next
            new_head = swap_node.next
            swap_node.next = head
            head.next = after_swap_node
            new_head.next = after_head
            return new_head