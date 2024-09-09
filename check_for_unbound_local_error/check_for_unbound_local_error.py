

def func_a(data_list):
    print('func_a')

    for data in data_list:
        if data == 5:
            result = data

    assert 'result' in locals(), 'data is not found'
    print(result)
    print()

def func_b(data_list):
    print('func_b')
    result = None
    for data in data_list:
        if data == 5:
            result = data

    assert result is not None, 'data is not found'
    print(result)
    print()





# data_list = [x for x in range(10)]
data_list = []

# func_a(data_list)
func_b(data_list)