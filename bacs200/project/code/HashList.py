class HashList:
    def __init__(self, length):
        self.hlist = [None] * length
        self.len = length

    def print(self):
        print(self.hlist)

    def hashfunction(self, item):
        return item % self.len

    def rehashfunction(self, oldpos):
        return (oldpos + 1) % self.len

    def contains(self, item):
        for i in self.hlist:
            if(i==item):
                return True
        return False
                    
    def put(self, item):
        hashvalue = self.hashfunction(item)
        if self.hlist[hashvalue] == None:
            self.hlist[hashvalue] =item
        elif self.hlist[hashvalue]!=None:
            return self.put2(hashvalue+1,item,hashvalue,0)

    def put2(self, hashvalue,item,origin,counter):
        if self.hlist[hashvalue]==None:
            self.hlist[hashvalue]=item
        elif self.hlist[hashvalue]!=None:
            if hashvalue==origin:
                return print("error")
            if hashvalue == self.len-1:
                return self.put2(0,item, origin, counter)
            else:
                return self.put2(hashvalue+1,item,origin,counter)

    def items(self):
        string = ""
        for i in self.hlist:
            if i != None:
                string += str(i) + ", "
        return string


# test Hash List 
hashlist = HashList(5)
hashlist.put(6)
hashlist.put(8)
hashlist.put(14)
print(hashlist.contains(6))
hashlist.print()
print(hashlist.items())
