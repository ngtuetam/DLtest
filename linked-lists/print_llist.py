# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def printLinkedList(head):
    if head is None:
        return None
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
    