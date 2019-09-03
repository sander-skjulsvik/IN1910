def median(data):
    '''
    Returns a sorted list

    Arguments
    -------------
    data : (list: (int, float), tuple: (int, float))
        list od data to be sorted
    Returns
    -------------
    list
        sorted list
    '''
    if len(data) == 0:
        raise ValueError('data list cant be empty')
    _data = list(data)
    _data.sort()
    n = len(_data)
    if n % 2 == 0:
        p, m = int(n/2+0.5), int(n/2-0.5)
        return (_data[p]+_data[m])/2
    else:   
        return _data[len(_data)//2]

# def median(data):
#     """Returns the median of a dataset."""
#     data.sort()
#     return data[len(data)//2]

def test_median():
    # #situation: one element list
    data = [8]
    expected_val = 8
    calculated_value = median(data)
    msg = f'expected_val = {expected_val}, calculated_value = {calculated_value}, data = {data}'
    assert expected_val == calculated_value, msg


    # #situation: two element list
    data = [8, 6]
    expected_val = (8+6)/2
    calculated_value = median(data)
    msg = f'expected_val = {expected_val}, calculated_value = {calculated_value}, data = {data}'
    assert expected_val == calculated_value, msg

    #situation: unchanged original data
    data = [2,3,1]
    expected_val = [2,3,1]
    calculated_value = median(data)
    
    msg = f'expected_val = {expected_val}, calculated_value = {calculated_value}, data = {data}'
    assert expected_val == data, msg

    #situation: raising an error if the input is empty list/tuple


if __name__ == "__main__":
    # print(median([11, 3, 1, 5, 3]))
    test_median()
    
    