import random
import time 



class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

def quick_sort(array, start, end): #array = [10,2,34,3,5,2,76,7,4,8]
    pass

def insertion_sort(array):
    pass

def merge_sort(array):
    pass

def bfs(root, target):
    pass

def minimax(root):
    pass


if __name__ == "__main__":
    #root = BinarySearchTreeNode(4)
    #nodes = [1, 5, 6, 9, 8, 7, 3, 2]
    #root.insert_nodes(nodes, root)
    #array = [10,2,34,3,5,2,76,7,4,8]
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
    #print(f"nodes: {nodes}")
    #print(f"array: {array}")
    #print(func_dict[11](root, 7))
    #print(func_dict[1](array))

    array = shuffle_cards(10)
    #loading(3, 0.5, ".", "Generating")
    #print(f"\nYour items are: {array}")
    #time.sleep(0.5)
    #loading(3, 1, ".", "Sorting")
    #sorted = func_dict[2](array)
    #print(f"\nYour sorted items are: {func_dict[1](array)}")
    print(array)
    quick_sort(array, 1, len(array)-1)
    print(array)

