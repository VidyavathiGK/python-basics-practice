from collections import deque


class Stack:
    """Last-In, First-Out (LIFO) stack implementation."""

    def __init__(self):
        self._items: list = []

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


class Queue:
    """First-In, First-Out (FIFO) queue implementation."""

    def __init__(self):
        self._items: deque = deque()

    def enqueue(self, item) -> None:
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    stack = Stack()
    stack.push("first")
    stack.push("second")
    print("Stack pop:", stack.pop())

    queue = Queue()
    queue.enqueue("job_1")
    queue.enqueue("job_2")
    print("Queue dequeue:", queue.dequeue())
