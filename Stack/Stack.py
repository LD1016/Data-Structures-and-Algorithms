class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 

class Stack: 
    def __init__(self):
        self.top = None 
        self.bottom = None
        self.length = 0

    def stringStack(self):
        temp = self.top 
        result = []
        while temp is not None:
            result.append(temp.data) 
            temp = temp.next
        return print(result)

    def peek(self):
        if self.length == 0:
            return None
        return self.top.data

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode 
            self.bottom = self.top 
            self.length += 1
            return self.stringStack()
        temp = self.top
        self.top = newNode 
        self.top.next = temp 
        self.length += 1
        return self.stringStack()

    def pop(self):
        result = None
        if self.length == 0: 
            return print('Stack is empty!')
        if self.length == 1:
            result = self.top.data
            self.top = None 
            self.bottom = None 
        else:
            result = self.top.data
            self.top = self.top.next
        self.length -= 1
        return result

myStack = Stack()
myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.push(20)
myStack.push(25)
myStack.push(30)
print(myStack.pop())
myStack.stringStack()
print(myStack.peek())
print(myStack.pop())
myStack.stringStack()
print(myStack.pop())
myStack.stringStack()
