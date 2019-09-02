
def bubble_sort(list_to_order):
    '''

    '''
    n = len(list_to_order)
    for j in range(n-1):
        for i in range(0,n-1):
            # print(f'list_to_order = {list_to_order}, i = {i}, j = {j}')
            greater = list_to_order[i]
            smaller = list_to_order[i+1]
            if list_to_order[i] > list_to_order[i+1]:            
                list_to_order[i] = smaller
                list_to_order[i+1] = greater

    return list_to_order

def test_bubble_sort():

    # situation: basic
    test_list = [4, 2, 3, 7, 1, 5]
    expected_list = [1, 2, 3, 4, 5, 7]
    ordered_list = bubble_sort(test_list)
    msg = f'situation: general\ntest_list = {test_list}, expected_list = {expected_list} != {ordered_list} = ordered_list'
    assert expected_list== ordered_list, msg

    # situation: empty list
    test_list = []
    expected_list = []
    ordered_list = bubble_sort(test_list)
    msg = f'situation: empty list\ntest_list = {test_list}, expected_list = {expected_list} != {ordered_list} = ordered_list'
    assert expected_list == ordered_list, msg

    # situation: one element
    test_list = [8]
    expected_list = [8]
    ordered_list = bubble_sort(test_list)
    msg = f'situation: one element\ntest_list = {test_list}, expected_list = {expected_list} != {ordered_list} = ordered_list'
    assert expected_list == ordered_list, msg


if __name__ == "__main__":
    test_bubble_sort()

    # test_list = [6,5,4,3,2,1]
    # print(bubble_sort(test_list))

    

