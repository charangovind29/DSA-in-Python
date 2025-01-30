from implementationofStackUsingSLL import *
class stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count -=1
    def size(self):
        return self.item_count
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(50)
s.push(39)
print('Top element is : ',s.peek())
s.pop()
print('Top element is : ',s.peek())
print(s.size())