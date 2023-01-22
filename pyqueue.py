class Queue:
    def __init__(self) -> None:
        self.items = []
        self.front_index = 0
    
    def __compress(self):
        new_list = []
        for i in range(self.front_index, len(self.items)):
            new_list.append(self.items[i])
        
        self.items = new_list
        self.front_index = 0
    
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Attempt to dequeue an empty queue")
        
        if self.front_index * 2 > len(self.items):
            self.__compress()

        item = self.items(self.front_index)
        self.front_index += 1
        return item
    
    def enter_que(self, item):
        self.items.append(item)
    
    def front(self):
        if self.is_empty():
            raise RuntimeError("Attempt to dequeue an empty queue")
        
        return self.items[self.front_index]
    
    def is_empty(self):
        return self.front_index == len(self.items)
