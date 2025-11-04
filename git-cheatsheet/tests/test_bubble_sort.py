def test_bubble_sort():
    from exercises.python.bubble_sort import bubble_sort

    # Test case 1: Regular case
    array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(array)
    assert sorted_array == [11, 12, 22, 25, 34, 64, 90]

    # Test case 2: Already sorted
    array = [1, 2, 3, 4, 5]
    sorted_array = bubble_sort(array)
    assert sorted_array == [1, 2, 3, 4, 5]

    # Test case 3: Reverse order
    array = [5, 4, 3, 2, 1]
    sorted_array = bubble_sort(array)
    assert sorted_array == [1, 2, 3, 4, 5]

    # Test case 4: Empty array
    array = []
    sorted_array = bubble_sort(array)
    assert sorted_array == []

    # Test case 5: Single element
    array = [42]
    sorted_array = bubble_sort(array)
    assert sorted_array == [42]

    # Test case 6: Duplicates
    array = [3, 1, 2, 3, 1]
    sorted_array = bubble_sort(array)
    assert sorted_array == [1, 1, 2, 3, 3]