class node:
    def __init__(self,item=None,priority=None,next=None):
        self.item = item
        self.priority = priority
        self.next = next

class priorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0
    
    def push(self,data,priority):
        n = node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and priority>temp.next.priority:
                temp = temp.next
            n.next = temp.next 
            temp.next = n
        self.item_count += 1
        
    def is_empty(self):
        return self.start == None
    
    def pop(self):
        if self.is_empty():
            raise IndexError('PriorityQueue is empty!')
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
    
    def size(self):
        return self.item_count



        
p = priorityQueue()
p.push('charan',1)
p.push('rakesh',2)
p.push('sanjay',4)
p.push('venky',3)
p.push('srujan',7)
p.push('deepthi',5)
while not p.is_empty():
    print(p.pop())
print(p.size())

        




    