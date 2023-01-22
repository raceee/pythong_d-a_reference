'''all complexities in the stack are O(1)'''

class Stack:
    # LIFO
    def __init__(self) -> None:
        self.items = []
    
    def pop(self): # 0(1)
        if self.is_empty():
            raise RuntimeError("Attempt to pop and empty stack")
        
        top_index = len(self.items) - 1
        item = self.items[top_index]
        del self.items[top_index]
        return item
    
    def push(self, item): # O(1)
        self.items.append(item)
    
    def top(self): # O(1)
        if self.is_empty():
            raise RuntimeError("Attempt to pop and empty stack")
        
        top_index = len(self.items) - 1
        return self.items[top_index]
    
    def is_empty(self): # O(1)
        return len(self.items) == 0
