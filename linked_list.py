class LinkedList:
    class __Node:
        def __init__(self,item, next) -> None:
            self.item = item
            self.next = next
        
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setNext(self, next):
            self.next = next
        
        def setItem(self, item):
            self.item = item
    
    def __init__(self,contents=[]) -> None:
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0
        for e in contents:
            self.append(e)

    def append(self, item): # O(1)
        node = LinkedList.__Node(item)
        self.last.setNext(node) # gets the last node in the list and sets its .setNext to the appended node
        self.last = node # sets the linked lists last node to the newly created one
        self.numItems += 1

    def insert(self,index, item): # O(n) but inserting at the beggining is O(1) since there are no terms to iterate over
        cursor = self.first
        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)

    def __getitem__(self, index): # requires a linear search and thus is O(n)
        if index >= 0 and index < len(self.contents):
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            return cursor.getItem()
        raise IndexError("Index out of range")
    
    def __setitem__(self, index, item): # requires a linear search and thus is O(n)
        if index >= 0 and index < len(self.contents):
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
            return cursor.setItem(item)
        raise IndexError("Index out of range")

    def __add__(self, other_list): # O(n) where n is the total amount of items in both lists
        if type(self) != type(other_list):
            raise TypeError("list to be catted is not of type 'LinkedList'")
        result = LinkedList()
        cursor = self.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
        cursor = other_list.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
        return result