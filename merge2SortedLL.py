def sortTwoLists(first, second):
    if first==None:
        return second
    if second==None:
        return first
    temp = t = Node(-1)
    while first and second:
        if first.data<=second.data:
            t.next = first
            first = first.next
        else:
            t.next = second
            second = second.next
        t = t.next
    if first==None:
        t.next = second
    elif second==None:
        t.next = first
    return temp.next
