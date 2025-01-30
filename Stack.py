class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class Stack:
    def __init__(self,start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self,data):
        n = node(data,self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError('Stack is empty!')
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError
    
    def size(self):
        return self.item_count
    

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print('Top element is ',stack1.peek())
print('Popped element is = ',stack1.pop())
print('Top element is ',stack1.peek())
