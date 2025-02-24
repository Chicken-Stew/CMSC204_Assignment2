# This program uses a Binary Search Tree structure

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Inserting a new node
    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while node:
                if value < node.value:
                    if node.left is None:
                        node.left = new_node
                        return
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        return
                    node = node.right

    # Searching for a value in the tree
    def search(self, value):
        node = self.root
        while node is not None:
            if node.value == value:
                print(f"Found in data: {value}")
                return
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        print(f"Not found in data: {value}")

    # Deleting an existing node in the tree
    def delete(self, value):
        node = self.root
        parent = None
        while node is not None and node.value != value:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        if node is not None:
            if node.left is None and node.right is None:
                if node != self.root:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None  # Deleting tree without children
            elif node.left is not None and node.right is not None:
                successor_parent = node 
                successor = node.right
                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left
                node.value = successor.value
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
            else:
                if node.left is not None:
                    child = node.left
                else:
                    child = node.right
                
                if node != self.root:
                    if parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                else:
                    self.root = child

# EXAMPLE: INSERTING
tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
# Inserting the next levels of the tree
tree.insert(4)
tree.insert(2)
tree.insert(8)
tree.insert(6)
tree.insert(45)

# EXAMPLE: SEARCHING
tree.search(45) # Should be in the data
tree.search(100) # Should not be in the data

# EXAMPLE: DELETING
tree.delete(8)
print(f"In the place of 8: {tree.root.right.right.value}") # This should be 45 since 8 was deleted

tree.delete(2)
while True:
    try:
        print(f"In the place of 2: {tree.root.left.left.value}") # This should be Null since 2 was deleted
    except AttributeError:
        print("No value exists.")
        break
