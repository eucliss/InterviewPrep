from LinkedList import LinkedList

def init_runner(ll,k):
    runner = ll.head
    for i in range(1, k):
        if not runner or not runner.next:
            return runner
        runner = runner.next
    return runner

def kth_to_last(ll, k):
    runner = init_runner(ll, k)
    key = ll.head
    if runner.next == None:
        return runner
    while runner.next != None:
        runner = runner.next
        key = key.next
    return key

#
# def kth_to_last(ll, k):
#     runner = current = ll.head
#     for i in range(k):
#         if runner is None:
#             return None
#         runner = runner.next
#
#     while runner:
#         current = current.next
#         runner = runner.next
#
#     return current

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))
