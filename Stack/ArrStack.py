class ArrStack:
    def __init__(self):
        self.arr = []
        self.length = 0
    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        if self.length == 0:
            return None
        return self.arr[self.length - 1]
    
    def pop(self):
        if self.length == 0:
            return None
        result = self.arr[self.length - 1]
        del self.arr[self.length - 1]
        self.length -= 1
        return result

    def push(self, data):
        self.arr.append(data)
        self.length += 1

mystack = ArrStack()
mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')
print(mystack)
x = mystack.peek()
print(x)
mystack.pop()
print(mystack)