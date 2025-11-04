def bubble_sort(array):
    for x in range(len(array)):
        swap = False
        for y in range(len(array)-1-x):
            if array[y+1] < array[y]:
                temp = array[y+1]
                array[y+1] = array[y]
                array[y] = temp
                swap = True
        if not swap:
            break
    return array