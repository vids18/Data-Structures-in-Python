# import sys
class Node:
    
    #int data
    #Node next
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        #next = None
        
class Linkedlist:
    
    nodeCount = 0
    def __init__(self):
        self.head = None
        self.tail = None
    
    def IsEmpty(self):
        if(self.nodeCount == 0):
            return True
        else:
            return False
        
    def CreateNode(self, data):
        Abc = Node(data)
        return Abc
    
    def AddNode(self, data):
        
        Pqr = self.CreateNode(data)
        
        if (self.IsEmpty()):
            self.head=Pqr
            self.tail = Pqr
        else:
            self.tail.next = Pqr
            self.tail = Pqr
        
        self.nodeCount = self.nodeCount + 1
        
#perform insertion operations on the linkedlist
        
        #insert at head
    def insertAtHead(self, data):
        newNode = Node(data)
        temp =self.head
        self.head = newNode
        newNode.next= temp
        self.nodeCount = self.nodeCount + 1
        return newNode

    def insertNode(self, data, pos):
        if (pos==1):
            Abc = self.insertAtHead(data)
        
        elif(pos==self.nodeCount):
            Abc = self.insertAtTail(data)
        
        else:
            Abc = Node(data)
            #print(Abc.data)
            temp = self.head
            current = temp
                
            for i in range(pos-1):
                temp = temp.next
                current = temp
            #print(current.data)    
            Abc.next= temp.next
            temp.next = Abc
            #temp = Abc
            self.nodeCount = self.nodeCount + 1
        #print(Abc.data)
    
    def insertAtTail(self,data):
        newNode = Node(data)
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        
        temp.next= newNode
        self.nodeCount = self.nodeCount + 1
        return newNode
                
# perform deletion operations on the linkedlist
        
    def delete(self,pos):
        if (pos==1):
            temp = self.head
            temp = temp.next
            self.head = temp
            self.nodeCount = self.nodeCount -1
            #print(self.nodeCount)
        
        elif (pos==self.nodeCount):
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            temp.next= None
            self.nodeCount = self.nodeCount - 1
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            temp.next = temp.next.next
            self.nodeCount = self.nodeCount - 1
        
            
                      
    
    def Display(self):
        temp = self.head
        #print(self.nodeCount)
        for i in range(self.nodeCount):
            print(temp.data,end="->")
            temp = temp.next

    
if __name__ == '__main__':
    ll = Linkedlist()
    ll.AddNode(10)
    ll.AddNode(60)
    ll.AddNode(50)
    ll.AddNode(30)
    ll.AddNode(100)
    #ll.Display()
    
    ll.insertNode(20, 1)
    ll.insertNode(200,3)
    ll.insertNode(3, 7)
    ll.Display()
    
    print("")
    
    ll.delete(1)
    ll.delete(3)
    ll.delete(5)
    ll.Display()
    
    