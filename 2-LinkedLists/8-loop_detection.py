from LinkedList import LinkedList

def loop_detection(ll):
    runner = ll.head
    seen = runner.data
    while True:
        if runner.next == None:
            return None
        runner = runner.next
        if runner.data is in seen:
            return runner
        seen.append(runner.data)
