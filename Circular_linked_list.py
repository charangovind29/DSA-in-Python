class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self,last=None):
        self.last = last

    def is_empty(self):
        if self.last is None:
            print('Circular linked list is empty!')
        else:
            print('The Circular linked list is not empty.')

    def insert_at_first(self,data):
        n = node(data)
        if self.last is None:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self,data):
        n=node(data)
        if self.last is None:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n            

    def search(self,data):
        if self.last is None:
            return None
        temp = self.last.next
        while temp is not self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None            
    
    def insert_after(self,temp,data):
        if temp is not None:
            n= node(data,temp.next)
            temp.next = n
            if temp==self.last:
                self.last = n
        
    def print_list(self):
        temp = self.last
        while temp!=self.last:
            print(temp.item,end=' ')
            temp = temp.next
        print(temp.item)

    def delete_at_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_at_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp!=self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

mylist = CLL()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.print_list()



