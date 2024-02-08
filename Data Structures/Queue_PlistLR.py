class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Queue_PlistLR:
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self.items[0]
	
    def size(self):
        return len(self.items)
    
    def __str__(self):
        str_q = ""
        
        for e in self.items:
            str_q+=str(e)+" "
            
        return str_q.strip()    
        