class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
            return
        curr_node = self.root
        while True:
            if curr_node.val > data:
                if curr_node.left is None:
                    curr_node.left = node
                    return
                else:
                    curr_node = curr_node.left
            elif curr_node.val < data:
                if curr_node.right is None:
                    curr_node.right = node
                    return
                else:
                    curr_node = curr_node.right

    def printTree(self):
        result = []
        if self.root is not None:
            self.printHelper(self.root, result)
        return print(result)

    def printHelper(self, tree, result):
        if tree is not None:
            self.printHelper(tree.left, result)
            result.append(tree.val)
            self.printHelper(tree.right, result)


test = Tree()
test.insert(8)
test.insert(10)
test.insert(6)
test.insert(12)
test.insert(5)
test.printTree()
