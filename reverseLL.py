def reverseLinkedList(head):
    prev = None
    while head!=None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
