class Deque:
    def __init__(self):
        self.items = []
        self.item_count = 0

    def  is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self,data):
        self.items.insert(0,data)
        self.item_count+=1
    
    def insert_rear(self,data):
        self.items.append(data)
        self.item_count += 1
    
    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('Deque is empty!')
        self.item_count -= 1

    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError('Deque is empty!')
        self.item_count -= 1
        
    def get_front(self):
        return self.items[0]
    
    def get_rear(self):
        return self.items[-1]

    def size(self):
        return self.item_count
    

#Driver code

d = Deque()
print(d.is_empty())
d.insert_front(10)
d.insert_rear(20)
d.insert_front(15)
d.insert_rear(50)
print(f'front element is {d.get_front()} Rear element is {d.get_rear()}')
print(d.size())
d.delete_front()
d.delete_rear()
print(d.is_empty())
print(f'front element is {d.get_front()} Rear element is {d.get_rear()}')
print(d.size())