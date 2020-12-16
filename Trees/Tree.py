class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


class Tree:
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
        result = []
        if self.root != None:
            self.printt(self.root, result)
        print(result)
# Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node, result):
        if curr_node != None:
            self.printt(curr_node.left, result)
            result.append(curr_node.value)
            self.printt(curr_node.right, result)


bst = Tree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()
