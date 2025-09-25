class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

def quick_sort(array):
    pass

def bubble_sort(array):
    for x in range(len(array)):
        for y in range(len(array)-1-x):
            if array[y+1] < array[y]:
                temp = array[y+1]
                array[y+1] = array[y]
                array[y] = temp
    return array

def insertion_sort(array):
    pass

def merge_sort(array):
    pass

def binary_search_array(array, target):
    print("performing binary search")
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return f"Target found at index {mid}"
    return "Target not found"



def binary_search_tree(root, target):
    depth = 0
    curr = root
    while curr:
        if curr.val < target:
            curr = curr.right
        elif curr.val > target:
            curr = curr.left
        elif curr.val == target:
            return f"Target found at depth {depth}"
        depth += 1
    return f"Target not found"

def linear_search(array, target):
    print("performing linear search")
    for i in range(len(array)):
        if array[i] == target:
            return f"Target found at index {i}"
    return "Target not found"

def bfs(root, target):
    pass

def dfs_preorder(root, target, depth=0, stack=[]):
    if root:
        stack.append(root.val)
        if root.val == target:
            print(stack)
        dfs_preorder(root.left, target, depth+1)
        dfs_preorder(root.right, target, depth+1)
        stack.pop()
        

def dfs_inorder(root, target, depth=0, stack=[]):
    if root:
        stack.append(root.val)
        dfs_inorder(root.left, target, depth+1)
        if root.val == target:
            print(stack)
        dfs_inorder(root.right, target, depth+1)
        stack.pop()

def dfs_postorder(root, target, depth=0, stack=[]):
    if root:
        stack.append(root.val)
        dfs_postorder(root.left, target, depth+1)
        dfs_postorder(root.right, target, depth+1)
        if root.val == target:
            print(stack)
        stack.pop()
        

def minimax(root):
    pass


if __name__ == "__main__":
    root = BinarySearchTreeNode(4)
    nodes = [1, 5, 6, 9, 8, 7, 3, 2]
    root.insert_nodes(nodes, root)
    array = [10,2,34,3,5,2,76,7,4,8]
    target = 7
    func_dict = {
        1: quick_sort,
        2: bubble_sort,
        3: insertion_sort,
        4: merge_sort,
        5: binary_search_array,
        6: binary_search_tree,
        7: linear_search,
        8: bfs,
        9: dfs_preorder,
        10: dfs_inorder,
        11: dfs_postorder
    }
    print(f"nodes: {nodes}")
    print(func_dict[11](root, 7))


