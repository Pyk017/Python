def sum_of_numbers(list_of_num, filter_fun = None):
    if filter_fun is None:
        return  sum(list_of_num)
    else:
        return sum(filter_fun(list_of_num))


def even(data):
    l = [i for i in data if i % 2 == 0]
    return l


def odd(data):
    l = [i for i in data if i % 2 != 0]
    return l


sample_data = range(1, 11)
print(sum_of_numbers(sample_data, even))
