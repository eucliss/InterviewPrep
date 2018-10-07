from LinkedList import LinkedList

def intersection(A, B):
    r1 = A.head
    r2 = B.head
    while r1.next is not None:
        while r2.next is not None:
            if r1 == r2:
                return r1
            r2 = r2.next
        r1 = r1.next
    return None
