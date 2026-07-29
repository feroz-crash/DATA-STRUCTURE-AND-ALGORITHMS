class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def printlist(self):
        current=self.head
        while current:
            print(current.data,end="-->")
            current=current.next
        print("None")
ll=linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)    
ll.printlist()