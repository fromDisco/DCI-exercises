def func_val_error():
    test_string = "hey"
    # provoke ValueError
    convert = int(test_string)
    return convert

def func_type_error():
    test_string = "hey"
    result = test_string + 4
    return result
