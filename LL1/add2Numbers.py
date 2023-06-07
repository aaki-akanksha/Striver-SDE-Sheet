def addTwoNumbers(head1, head2):
    if head1==None:
       return head2
    if head2==None:
        return head1
    c = 0
    temp = t = Node(-1)
    while c or head1 or head2:
        sum = c
        if head1:
            sum+= head1.data
            head1 = head1.next
        if head2:
            sum+= head2.data
            head2 = head2.next
        c = sum//10
        temp.next = Node(sum%10)
        temp = temp.next
    return t.next
