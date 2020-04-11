class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None

    def __str__(self):
        return self.data

class DLinkedList:
    def __init__(self):
        self.head = None

    def add(self, newdata):
        new_node = Node(newdata) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node

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

    def deleteNode(self, dele):  
        if self.head is None or dele is None: 
           return  
        if self.head == dele: 
            self.head = dele.next
        if dele.next is not None: 
            dele.next.last = dele.last
        if dele.last is not None: 
            dele.last.next = dele.next

    def insert(self, prev_node, new_data): 
        if prev_node is None: 
            print("This node doesn't exist in DLL") 
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node 
        new_node.prev = prev_node 
        if new_node.next is not None: 
            new_node.next.prev = new_node


    def append(self, new_data): 
        new_node = Node(data = new_data) 
        last = self.head 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        while (last.next is not None): 
            last = last.next 
        last.next = new_node 
        new_node.prev = last


    def Listprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
            if(printval.data==self.head.data):  #because in doubly linked lists
                break                           #this would usually loop forever
            
    def pop(self):
        last = self.head
        while(last.next):
            last = last.next
        temp = last.data
        last.last.next=self.head
        self.deleteNode(last)
        return temp

"""     Testing the functions above
llist = DLinkedList()

e1 = Node("mon")
e2 = Node("tues")
e3 = Node("wed") 
e4 = Node("thur")
e5 = Node("fri")
e6 = Node("bad day")

llist.add(e2)
llist.add(e1)
llist.append(e4)
llist.insert(llist.head.next,e3)
llist.add(e5)

llist.insert(llist.head.next.next,e6)
print(llist.pop(e6), " should be deleted")

llist.Listprint() """


