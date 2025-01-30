class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index+=1
        self.items.insert(index,(data,priority))
    
    def pop(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')
        else:
            return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)

#driver code
p = PriorityQueue()
p.push('charan',1)
p.push('rakesh',2)
p.push('sanjay',4)
p.push('venky',3)
p.push('srujan',7)
p.push('deepthi',5)
while not p.is_empty():
    print(p.pop())
print(p.size())

