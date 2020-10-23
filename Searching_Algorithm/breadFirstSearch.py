class TreeNode: 
    def __init__(self, data):
        self.left = None 
        self.right = None
        self.value = data 
    
class BinarySearchTree: 
    def __init__(self):
        self.root = None 

    def insert(self, data):
        newNode = TreeNode(data)
        if self.root is None: 
            self.root = newNode 
            return 
        currNode = self.root 
        while True: 
            # Check if newNode should go to leftside
            if currNode.value > data: 
                if currNode.left is None:
                    currNode.left = newNode
                    return 
                else: 
                    currNode = currNode.left 
            elif currNode.value < data:
                if currNode.right is None:
                    currNode.right = newNode
                    return 
                else: 
                    currNode = currNode.right
                
    def lookup(self, data):
        if self.root is None: 
            return False 
        currNode = self.root 
        while currNode is not None:
            if data == currNode.value:
                return True 
            elif data < currNode.value:
                currNode = currNode.left 
            elif data > currNode.value:
                currNode = currNode.right 
        return False

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
#Inorder Traversal (We get sorted order of elements in tree)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)

    # Bread First Search 
    def breadFirstSearch(self):
        result = []
        currNode = self.root
        queue = [currNode]
        while len(queue):
            currNode = queue[0]
            del queue[0]
            if currNode.left is not None:
                queue.append(currNode.left)
            if currNode.right is not None:
                queue.append(currNode.right)
            result.append(currNode.value)
        return result
    
    # Bread First Search 
    def breadFirstSearchR(self, queue, result):
        if len(queue) == 0:
            return result 
        currNode = queue[0]
        del queue[0]
        if currNode.left is not None:
            queue.append(currNode.left)
        if currNode.right is not None:
            queue.append(currNode.right)
        result.append(currNode.value)
        return self.breadFirstSearchR(queue, result)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

x = tree.lookup(170)
print(x)  
print(tree.breadFirstSearch())
print(tree.breadFirstSearchR([tree.root],[]))
