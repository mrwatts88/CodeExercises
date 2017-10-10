class Node(object):
    
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.nextNode
    
    def setNext(self, newNext):
        self.nextNode = newNext
        
class myLinkedList(object):
    
    def __init__(self, head=None):
        self.head = head
        
    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
    
    def remove(self, data):
        current = self.head
        previous = None
        found = False
        
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if current is None:
            raise ValueError("Data is not in the list.")
        
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def printMe(self):
        n = self.head
        if n is None:
            print("List is empty")
            
        while n.getNext() != None:
            print(n.getData())
            n = n.getNext()
            
        print (n.getData())    