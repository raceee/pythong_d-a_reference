class HashSet:
    class __Placeholder:
        def __init__(self) -> None:
            pass

        def __eq__(self, __o: object) -> bool:
            return False
    
    def __remove(item, items):
        return
        
    def __init__(self, contents=[]) -> None:
        self.items = [None] * 10 
        self.numItems = 0
        for item in contents:
            self.add(item)
    
    def __add(item, items):
        idx = hash(item) % len(items)
        loc = -1

        while items[idx] != None:
            if items[idx] == item: # this item is already in the set
                return False
        
            if loc < 0 and type(items[idx]) == HashSet.__Placehodler:
                loc = idx
            
            idx = (idx + 1) % (len(items))
        if loc < 0:
            lox = idx
        items[loc] = item
        return True
    
    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newList)