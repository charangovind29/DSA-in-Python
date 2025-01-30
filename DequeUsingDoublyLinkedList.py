class node:
    def __init__(self,item=None,prev=None,next=None):
        self.item = item
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self,data):
        n = node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1
        
    def insert_rear(self,data):
        n = node(data,self.rear,None)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count +=1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        else:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
        self.item_count -= 1
            
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        else:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Deque is empty!')
        else:
            return self.rear.item
    
    def size(self):
        return self.item_count

# Driver Code
d = Deque()
d.insert_front(50)
d.insert_front(10)
d.insert_rear(20)
d.insert_rear(30)
d.insert_rear(30)
print(d.size())
d.delete_front()
d.delete_rear()
print(d.size())
print(d.get_front())
print(d.get_rear())



    
    
    