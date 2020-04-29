class Queue:
    def __init__(self):
        self.back = None
        self.queue = []


    def enqueue(self,data):                 #O(1)
        self.queue.append(data)
        if self.back is None:
            self.back = data

    def dequeue(self):                      #O(n)
        pop = self.queue[0]
        temp = []
        var = 1
        while (var<=len(self.queue)-1):
            temp.append(self.queue[var])
            var = var +1
        self.queue = temp
        self.back = self.queue[0]
        return pop

    def isEmpty(self):                      #O(1)
        if self.back is None:
            return True
        else:
            return False

    def size(self):                         #O(n)
        counter = 0
        for i in self.queue:
            counter = counter + 1
        return counter

#Tests the above functions
myQueue = Queue()
print(myQueue.isEmpty())
myQueue.enqueue('a')
myQueue.enqueue('b')
myQueue.enqueue('c')
myQueue.enqueue('d')
print(myQueue.isEmpty())
print(myQueue.dequeue())
print(myQueue.queue)
print(myQueue.size())
