class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Queues: 
    def __init__(self):
        self.first = None 
        self.last = None
        self.length = 0

    def stringQueue(self):
        temp = self.last 
        result = []
        while temp is not None:
            result.append(temp.data) 
            temp = temp.next
        return print(result)
    
    def printt(self):
        temp = self.first
        while temp != None:
            print(temp.data , end = '->')
            temp = temp.next
        print()
        print(self.length)

    def peek(self):
        if self.length == 0:
            return print('Queues is Empty!') 
        return self.first.data 

    def enqueue(self, data):
        newNode = Node(data) 
        if self.length == 0:
            self.first = newNode 
            self.last = self.first 
        else: 
            temp = self.last 
            self.last = newNode
            temp.next = self.last 
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return print('Queue is empty!')
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next 
        self.length -= 1


myq = Queues()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.printt()
myq.dequeue()
myq.printt()
x = myq.peek()
print(x)