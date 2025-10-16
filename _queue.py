from typing import Any
from collections import deque

"""
Think of a queue as people standing in line in a supermarket.
The first person to stand in line is also the first who can pay and leave the supermarket.

Basic operations we can do on a queue are:
- Enqueue: Adds a new element to the queue.
- Dequeue: Removes and returns the first (front) element from the queue.
- Peek: Returns the first element in the queue.
- isEmpty: Checks if the queue is empty.
- Size: Finds the number of elements in the queue.

"""

class Queue:
    def __init__(self):
        self.queue = deque()
        self.message: str = "Queue is empty!"

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)

    def dequeue(self) -> None:
        if self.is_empty():
            return self.message
        return self.queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def peek(self) -> Any:
        return self.message if self.is_empty() else self.queue[0]

    def size(self) -> int:
        return len(self.queue)


queue = Queue()



