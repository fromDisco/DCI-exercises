num_list = [1, 2, 3]


def get_sum(num_list):
    total = 0
    for i in num_list:
        total += i
    return total


def rec_sum(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[-1] + rec_sum(num_list[:-1]) 


print(get_sum(num_list))
print(rec_sum(num_list))
