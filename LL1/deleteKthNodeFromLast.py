def removeKthNode(head, k):
    if head==None or k==0:
        return head
    temp = Node(-1)
    temp.next = head
    s = f = temp
    for i in range(k):
        f = f.next
    while f.next!=None:
        f = f.next
        s = s.next
    s.next = s.next.next
    return temp.next
