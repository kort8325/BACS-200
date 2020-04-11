class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
class SLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
		

    def RemoveNode(self, Removekey):
        HeadVal = self.head
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None

    def search(self, searchKey): 
         
        current = self.head 
        # loop till current not equal to None 
        while current != None: 
            if current.data == searchKey: 
                return True # data found
            current = current.next
        return False

    def isEmpty(self):
        if(self.head is None):
            return(True)
        return(False)

    def size(self):
        counter = 0
        current=self.head
        while(current !=None):
            counter+=1
            current=current.next
        return(counter)

    def append(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head=NewNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewNode

    def index(self, searchKey):
        current = self.head
        counter = 0
        # loop till current not equal to None 
        while current != None:
            if current.data == searchKey: 
                return counter # data found
            counter += 1
            current = current.next
        return -1

    def insert(self, pos, newdata):
        if pos is None:
            print("no node with position: ", pos)
            return
        NewNode = Node(newdata)
        NewNode.next = pos.next
        pos.next = NewNode
        
    def Listprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next

    def pop(self):
        last = self.head
        while(last.next):
            last = last.next
        temp = last.data
        self.RemoveNode(last.data)
        return temp

"""     Testing the functions above
llist = SLinkedList()

e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed") 
e4 = Node("Thur")
e5 = Node("Fri")

llist.add(e1)
llist.append(e2)
llist.append(e3)
llist.append(e5)

llist.insert(llist.head.next.next, e4)

llist.Listprint()"""
