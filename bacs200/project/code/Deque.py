class Deque:
    def __init__(self):
        self.top = None
        self.front = None
        self.stack = []

    def addFront(self,data):                 #O(n)
        temp = []
        temp.append(data)
        for i in self.stack:
            temp.append(i)
        self.stack = temp
        self.front = data


    def addRear(self, data):                 #O(1)
            self.stack.append(data)
            self.top = data

    def removeFront(self):                   #O(n)
        pop = self.stack[0]
        temp = []
        var = 1
        while (var<=len(self.stack)-1):
            temp.append(self.stack[var])
            var = var +1
        self.stack = temp
        self.back = self.stack[0]
        return pop

    def removeRear(self):                    #O(n)
        temp1 = self.stack.pop()
        temp = ""
        for i in self.stack:
            if(i == temp1):
                break
            temp = i
        self.top = temp
        return(temp1)

    def isEmpty(self):                       #O(1)
        if self.front is None and self.top is None:
            return True
        else:
            return False

    def size(self):                         #O(n)
        counter = 0
        for i in self.stack:
            counter = counter + 1
        return counter

#Tests the above functions
deque = Deque()
print(deque.isEmpty())
deque.addFront('c')
deque.addRear('d')
deque.addFront('b')
deque.addFront('a')
print(deque.size())
print(deque.removeFront())
print(deque.removeRear())
print(deque.isEmpty())
print(deque.stack)



