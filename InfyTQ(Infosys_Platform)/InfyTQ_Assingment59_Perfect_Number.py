def check_perfect_number(number):
    if number < 6:
        return False
    else:
        ls = []
        for i in range(1, number):
            if number % i == 0:
                ls.append(i)

        if number == sum(ls):
            return True

        return False


def check_perfectno_from_list(no_list):
    ls = list(map(check_perfect_number, no_list))
    if not any(ls):
        return []
    return ls


perfect_list = check_perfectno_from_list([18, 6, 4, 2, 1, 28, 496])
print(perfect_list)