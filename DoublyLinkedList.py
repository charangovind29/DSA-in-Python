class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            print('The list is empty')
        else:
            print('The list is not empty')
    
    def insert_at_first(self,data):
        n = Node(None,data,self.start)
        if self.start is None:
            self.start = n
        else:
            self.start.prev = n
            self.start = n
    
    def insert_at_last(self,data):
        n = Node(None,data,None)
        if self.start is None:
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n
        
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def delete_at_first(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            self.start.next.prev = None
            self.start = self.start.next
        
    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp =self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next
        return
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next
    
    def search(self,data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next

    def insert_at_specific_position(self,position,data):
        n = Node(None,data,None)
        #inserting at beginning
        if position <= 0 and not self.start:
            if self.start:
                self.start.prev = n
            n.next = self.start
            return
        
        temp = self.start
        count = 0
        while temp.next and count<position-1:
            temp = temp.next
            count += 1
        
        # last node insertion
        if not temp.next and count<position-1:
            temp.next = n
            n.prev = temp
            return
        
        # middle
        n.next = temp.next 
        if temp.next:
            temp.next.prev = n
        n.prev = temp
        temp.next = n

mylist = DLL()
mylist.insert_at_first(10)
mylist.insert_at_first(10)
mylist.insert_at_last(30)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(10),20)
mylist.delete_at_first()
mylist.delete_at_last()
mylist.delete_item(10)
mylist.insert_at_specific_position(1,5)
mylist.insert_at_specific_position(4,6)
mylist.insert_at_specific_position(-1,3002)
mylist.print_list()

