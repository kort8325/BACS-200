class Stack:
    
    def __init__(self):
        self.top=None
        self.stack= []
        

    def push(self, data):              #O(1)
            self.stack.append(data)
            self.top = data

    def pop(self):                     #O(n)
        temp1 = self.stack.pop()
        temp = ""
        for i in self.stack:
            if(i == temp1):
                break
            temp = i
        self.top = temp
        return(temp1)

    def peek(self):                    #O(1)
        return(self.top)

    def isEmpty(self):                 #O(1)
        if(self.top is None):
            return True
        else:
            return False

    def size(self):                    #O(n)
        counter = 0
        for i in self.stack:
            counter = counter + 1
        return(counter)

""" Tests the above functions
newStack = Stack()
print(newStack.isEmpty())
newStack.push('a')
newStack.push('b')
newStack.push('c')
newStack.push('d')
print(newStack.peek())
newStack.pop()
print(newStack.stack)
print(newStack.isEmpty())
print(newStack.size())"""
