class MyArray: 
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item
    
    def shiftItems(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length -= 1


arr = MyArray()

arr.push('Hello! ')
arr.push('My')
arr.push('name')
arr.push('is')    
arr.push('Lance')
print(arr)

arr.get(2)
arr.pop()
print(arr)


print(arr.delete(3))
print(arr)