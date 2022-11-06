class Node():
    def __init__(self,data):
        self.data = data
        self.next = "NULL"
        self.prev = "NULL"
    
    def getData(self):
        return self.data
    


class LinkedList():
    def __init__(self):
        self.head = "NULL"
    
    def addNode_L(self,data):
        if self.head == "NULL":
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next != "NULL"):
                temp = temp.next
            temp.next = Node(data)
            temp.next.prev = temp


    
    def getLastNode(self):
        temp = self.head
        while(temp.next != "NULL"):
            temp = temp.next
        return temp

    def printNodes(self):
        temp = self.head
        counter = 1
        while(temp != "NULL"):
            print(f"{counter}.Node.data = {temp.data}")
            temp = temp.next

