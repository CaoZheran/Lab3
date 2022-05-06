import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 3, 4]
    test_arr = [1, 3, 4, 11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 3, 4]
    test_arr = [90, 64, 34, 25, 22, 12, 11, 4, 3, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_REQ_01():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 3, 4]
    test_arr = [90, 64, 34, 25, 22, 12, 11, 4, 3, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_REQ_02():

    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 3, 4, 9]
    result = 1

    result_return = Lab3.bubble_sort(input_arr, 0)

    assert (result == result_return)


def test_REQ_03():

    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = 2

    result_return = Lab3.bubble_sort(input_arr, 0)

    assert (result == result_return)

def test_REQ_04():

    input_arr = []
    result = 0

    result_return = Lab3.bubble_sort(input_arr, 0)

    assert (result == result_return)

def test_REQ_05():

    input_arr = [6.4, 34, 25, 12, 22, 11, 90, 1, 3, 4, 9]
    result = 3

    result_return = Lab3.bubble_sort(input_arr, 0)

    assert (result == result_return)


def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 3, 4]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


