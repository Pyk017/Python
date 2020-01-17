import string


def is_valid(name):
    if name[0] in string.digits or name[0] in '_':
        return False

    for i in name:
        if i in string.punctuation:
            return False

    return True


for _ in range(5):
    st = input()
    print("{} : {}".format(st, is_valid(st)))
