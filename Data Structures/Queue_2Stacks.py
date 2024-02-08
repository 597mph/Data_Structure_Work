import Stack_PlistLR

class Queue_2Stacks:
    def __init__(self):
        self.stack1 = Stack_PlistLR()
        self.stack2 = Stack_PlistLR()

    def is_empty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()

    def __str__(self):
        return str(self.stack1) + " " + str(self.stack2)

    def __len__(self):
        return self.size()

# Example Usage:
queue = Queue_2Stacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue)  # Output: Queue: 1 2 3
print("Size:", len(queue))  # Output: Size: 3

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # Output: Dequeued item: 1

print("Queue after dequeue:", queue)  # Output: Queue after dequeue: 2 3
print("Size after dequeue:", len(queue))  # Output: Size after dequeue: 2