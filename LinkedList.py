class ListNode:

    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getLast(self):
        return self.tail.val

    def getFirst(self):
        return self.head.val

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, val):
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head

        new_node = ListNode(val, self.head)
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def addLast(self, val):
        if not self.tail:
            self.head = ListNode(val)
            self.tail = self.head

        new_node = ListNode(val=val, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def removeFirst(self):
        if not self.head:
            return

        out = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

        return out

    def removeLast(self):
        if not self.tail:
            return

        out = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

        return out


class Stack:

    def __init__(self) -> None:
        self.arr = LinkedList()

    def peek(self):
        self.arr.getLast()

    def push(self, item):
        self.arr.addLast(item)

    def pop(self):
        return self.arr.removeLast()

    def isEmpty(self):
        return self.arr.isEmpty()


if __name__ == "__main__":

    stack = Stack()

    stack.push(10)
    stack.push(20)

    print(stack.pop())
    print(stack.pop())
    print(stack.isEmpty())
