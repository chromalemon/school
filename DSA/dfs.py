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