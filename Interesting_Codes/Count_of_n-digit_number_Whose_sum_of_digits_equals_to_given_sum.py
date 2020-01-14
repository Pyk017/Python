def count_digit_number(n, sumi):
    start = 10**(n-1)
    end = sumi * start
    count = 0
    for i in range(start, end+1):
        a = sum(list(map(int, str(i))))
        if a == sumi:
            print(i)
            count += 1

    return count


print(count_digit_number(3, 6))
