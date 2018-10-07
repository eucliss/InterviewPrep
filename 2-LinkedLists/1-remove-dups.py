from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None or ll.head.next is None:
        return ll
    iter = ll.head
    unique = []
    while iter is not None:
        if iter.value not in unique:
            unique.append(iter.value)
            prev = iter
            iter = iter.next
        else:
            del_next = prev
            prev = iter
            iter = iter.next
            ll.deleteNode(del_next)
    # print(unique)
    return ll

ll = LinkedList()
ll.generate(100, 0, 2)
print(ll)
remove_dups(ll)
print(ll)
#
# ll.generate(100, 0, 9)
# print(ll)
# remove_dups_followup(ll)
# print(ll)
