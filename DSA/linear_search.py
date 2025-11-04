def linear_search(array, target):
    print("performing linear search")
    for i in range(len(array)):
        if array[i] == target:
            return f"Target found at index {i}"
    return "Target not found"