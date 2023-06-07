def findMiddle(head):
    temp = head
    while temp and temp.next:
        temp = temp.next.next
        head = head.next
    return head
