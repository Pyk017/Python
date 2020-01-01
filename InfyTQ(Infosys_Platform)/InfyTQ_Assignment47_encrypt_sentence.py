vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']


def shift_vowel(st):
    st2 = ''
    for i in st:
        if i in vowel:
           st2 += i
        else:
            st2 = i + st2

    return st2


def encrypt_sentence(s):
    s = s.split()
    string2 = ''
    l = list(enumerate(s, 1))
    for i, j in l:
        if i % 2 == 0:
            string2 += shift_vowel(j)
        else:
            string2 += j[::-1]

        string2 += ' '

    return string2


string = input("Enter a String :- ")
print("Encrypted String is :- ", encrypt_sentence(string))
