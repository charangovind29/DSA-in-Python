class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_counts = 0

    def is_empty(self):
        return self.item_counts==0
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_counts += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_counts -=1 
    
    def get_front(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')
        else:
            return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.rear.item
    
    def size(self):
        return self.item_counts
    

q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())


            