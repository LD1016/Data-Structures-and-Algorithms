# class LinkList: 
#     def __init__(self, value):
#         self.head = {
#             'value': value,
#             'next': None
#         }
#         self.tail = self.head
#         self.length = 1
#     def __str__(self):
#         return str(self.__dict__)

#     def append(self, value):
#         # New node 
#         newNode = {
#             'value': value,
#             'next': None 
#         }
#         self.head['next'] = newNode 
#         self.tail = newNode 
#         self.length += 1

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0
    def __str__(self):
        return str(self.__dict__)

    def printList(self):
        result = []
        if self.head is None:
            return result 
        currHead = self.head 
        while currHead is not None:
            result.append(currHead.data)
            currHead = currHead.next 
        return result

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode 
            self.tail = self.head 
        else:
            self.head.next = newNode
            self.tail = newNode 
        self.length +=1 

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode 
            self.tail = self.head 
        else: 
            temp = self.head 
            self.head = newNode
            self.head.next = temp 
        self.length += 1
    
    def insert(self, index, value):
        newNode = Node(value)
        if index >= self.length:
            self.append(value)
            return print(self.printList())
        if index == 0:
            self.prepend(value)
            return print(self.printList())
        i = 0
        currHead = self.head
        while i < index-1:
            currHead = currHead.next
            i += 1
        temp = currHead.next 
        currHead.next = newNode 
        newNode.next = temp 
        return print(self.printList())

    def remove(self, index):
        if index >= self.length: 
            return print('Wrong index!')
        if index == 0:
            self.head = self.head.next
            return print(self.printList())
        i = 0
        currHead = self.head
        while i < index-1:
            currHead = currHead.next
            i += 1
        rest = currHead.next.next
        currHead.next = rest 
        return print(self.printList())
        
    def reverse(self):
        prev = None 
        self.tail = self.head 
        while self.head is not None: 
            tempHead = self.head 
            self.head = self.head.next 
            tempHead.next = prev 
            prev = tempHead 
        self.head = prev
        return print(self.printList())
    



myLinkList = LinkList()
myLinkList.append(10)
print('Head: {}, tail: {}, length: {}'.format(myLinkList.head.data, myLinkList.tail.data, myLinkList.length))
print(myLinkList.printList())
myLinkList.append(5)
print('Head: {}, tail: {}, length: {}'.format(myLinkList.head.data, myLinkList.tail.data, myLinkList.length))
print(myLinkList.printList())
myLinkList.prepend(18)
print('Head: {}, tail: {}, length: {}'.format(myLinkList.head.data, myLinkList.tail.data, myLinkList.length))
print(myLinkList.printList())
myLinkList.insert(1, 33)
myLinkList.insert(0, 15)
myLinkList.insert(2, 55)
myLinkList.reverse()
myLinkList.remove(0)
myLinkList.remove(1)
