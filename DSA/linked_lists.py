'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

### John Pork

class LinkedListNode: # define class LinkedListNode
    def __init__(self, val=None, next=None): # initialises node
        self.val = val # assigns value to val attribute
        self.next = next # assigns next node to next attribute
        
class BinaryTreeNode: # define class BinaryTreeNode
    def __init__(self, val=None, left=None, right=None): # initialising node
        self.val = val # assigns given value to val attr.
        self.left = left # left node from root assigned
        self.right = right # right node from root assigned

class LinkedList:
    def __init__(self, root): # initialises object
        
        self.root = root # assigns value to root attribute
        self.dummy = LinkedListNode(None, self.root)
        
    def add(self, node): # method to add node to the list
        curr = self.root # curr starts as the root
        while curr.next: # while there is still nodes to traverse
            curr = curr.next # set curr to the next node
        curr.next = node # at the end, set next to new node
        
    def add_in_order(self, node): # add items in ASC order
        curr = self.dummy # starting node is dummy, allows insertion behind root
        while curr.next and curr.next.val <= node.val: # stop at end of list or before val
            curr = curr.next # curr is next node
        if curr.next: # if not at end of list
            node.next = curr.next # new node's next is curr's next
            curr.next = node 
        else:
            curr.next = node
            #None, 7, 8, 9
            
    def delete_node_by_val(self, val):
        curr = self.dummy
        counter = 0
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
    def print_list(self): # method to print the items in the list
        curr = self.dummy.next
        while curr.next:
            print(curr.val, ", ", end="", sep="")
            curr = curr.next
        print(curr.val)
        
    def __str__(self):
        return f"Linked List with root val {self.dummy.next.val}"
        
    def __repr__(self):
        return f"root: {self.dummy.next}, val: {self.dummy.next.val}"
        
if __name__ == "__main__":
    import random
    
    items = [6, 7, 2, 9, 5, 4, 8, 1 ,3]
    random.shuffle(items)
    print(f"items: {items}")
    
    root1 = LinkedListNode(items[0])
    root2 = LinkedListNode(items[0])
    linked_list1 = LinkedList(root1)
    linked_list2 = LinkedList(root2)
    
    
    
    for item in items[1:]:
        node1 = LinkedListNode(item)
        node2 = LinkedListNode(item)
        linked_list1.add(node1)
        linked_list2.add_in_order(node2)
        
    print(f"Linked list: ", end="")
    linked_list1.print_list()
    
    print(f"Linked list in ASC order: ", end="")
    linked_list2.print_list()
    
    
    
    print(str(linked_list1))
    
    print(repr(linked_list1))
    
    print("-------\n")
    
    to_delete = 2
    
    print(f"Deleting node from sorted with val {to_delete}: ", end="")
    linked_list2.delete_node_by_val(to_delete)
    linked_list2.print_list()
    
    
            