Queue_2Stacks() utilizes two stacks to mimic the behavior of a queue. The enqueue operation is straightforward, pushing items to stack1. The dequeue operation involves transferring elements from stack1 to stack2 if stack2 is empty, then popping from stack2. The __str__ and __len__ methods allow the object to be printed and its size obtained using print() and len() functions, respectively.

Stack_2Queues() utilizes two queues to mimic the behavior of a stack. The push operation is achieved by enqueuing the item to the second queue, then transferring elements from the first queue to the second and back. The pop operation dequeues from the first queue. The __str__ and __len__ methods allow the object to be printed and its size obtained using print() and len() functions, respectively.

Developed by Maxwell Hauser
