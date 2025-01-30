class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
    
class SLL:
    def __init__(self,start=None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n = Node(data)
        if self.start is None:
            self.start = n
        else:
            n.next = self.start
            self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next 
            temp.next = n

    def search(self,data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
        return None

    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            temp.next = n
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next

    def delete_first(self):
        if self.is_empty():
            raise IndexError('The list is empty!')
        elif self.start.next == None:
            self.start = None
        else:
            self.start = self.start.next
            
    def delete_at_last(self):
        if self.is_empty():
            raise IndexError('List is empty!')
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self,data):
        if self.is_empty():
            raise IndexError('List is empty!')
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data



sll = SLL()
sll.insert_at_start(10)
sll.insert_at_start(20)
sll.insert_at_start(30)
sll.insert_at_start(40)
sll.insert_at_last(500)
sll.insert_after(sll.search(10),15)     
sll.print_list()     
sll.delete_first()
sll.delete_at_last()
sll.delete_item(10)
sll.print_list()             
for i in sll:
    print(i)