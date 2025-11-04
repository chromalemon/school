class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class BinarySearchTreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)

    def insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = BinarySearchTreeNode(val)
                else:
                    self.left.insert_node(val)
            elif val > self.val:
                if self.right is None:
                    self.right = BinarySearchTreeNode(val)
                else:
                    self.right.insert_node(val)
    @staticmethod
    def insert_nodes(vals, root):
        for i in vals:
            root.insert_node(i)