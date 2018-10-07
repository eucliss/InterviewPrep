# class Node(object):
#
#     def __init__(self, data=None, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
#
#
# class LinkedList(object):
#
#     def __init__(self, head=None):
#         self.head = head
#
#
#
# list = LinkedList()
# list.head = Node(8)
# print(list.head.data)
# list.head.next = Node(10, list.head)
# print(list.head.next.data)

from random import randint


class LinkedListNode:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def deleteNode(self,node):
        if node.next and node.next.next:
            node.next = node.next.next
        else:
            node.next = None


class DoublyLinkedList(LinkedList):

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value, None, self.tail)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self
