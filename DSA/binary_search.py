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