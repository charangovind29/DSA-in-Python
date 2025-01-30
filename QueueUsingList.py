class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('Queue is empty cannot pop!')
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Queue is empty!')
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Queue is empty!')
    def size(self):
        return len(self.items)

q1 = Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
print('Front element : ',q1.get_front())
print('Rear Element : ',q1.get_rear())
q1.dequeue()
print('Front element : ',q1.get_front())
print(f'Now the Queue has {q1.size()} elements')