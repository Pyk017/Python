def check_prime(number):
    if number == 2:
        return True
    i = 0
    for i in range(2, number):
        if number % i == 0:
            break

    return True if i == number-1 else False


def rotations(num):
    ls = list(map(int, str(num)))
    ls2 = []
    for i in range(len(ls)):
        ls.append(ls[0])
        ls.pop(0)
        ls2.append(int(''.join(map(str, ls))))

    print(ls2)
    ls2.insert(0, ls2[-1])
    ls2.remove(ls2[-1])
    print(ls2)
    return ls2


def get_circular_prime_count(limit):
    ls = []
    for i in range(1, limit):
        a = rotations(i)
        b = list(map(check_prime, a))
        if all(b):
            ls.append(i)

    return ls

rotations(179)
# print("Circular Prime Numbers are :- ", get_circular_prime_count(int(input("Enter the Limit :- "))))
