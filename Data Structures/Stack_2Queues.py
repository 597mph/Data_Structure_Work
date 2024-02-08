from collections import deque
import Queue_PlistLR

class Stack_2Queues:
    def __init__(self):
        self.queue1 = Queue_PlistLR()
        self.queue2 = Queue_PlistLR()

    def is_empty(self):
        return self.queue1.isEmpty()

    def size(self):
        return self.queue1.size()

    def push(self, item):
        self.queue2.enqueue(item)
        while not self.queue1.isEmpty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.queue1.dequeue()

    def __str__(self):
        return str(self.queue1)

    def __len__(self):
        return len(self.queue1)

# Example Usage:
stack = Stack_2Queues()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack)  # Output: Stack: 3 2 1
print("Size:", len(stack))  # Output: Size: 3

pop_item = stack.pop()
print("Popped item:", pop_item)  # Output: Popped item: 3

print("Stack after pop:", stack)  # Output: Stack after pop: 2 1
print("Size after pop:", len(stack))  # Output: Size after pop: 2