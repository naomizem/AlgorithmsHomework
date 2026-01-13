#4
class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(tree, value):
    if tree.root is None:
        tree.root = Node(value)
        return

    curr = tree.root
    while True:
        if tree.key(value) < tree.key(curr.value):
            if curr.left is None:
                curr.left = Node(value)
                return
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = Node(value)
                return
            curr = curr.right