from collections import Counter


def max_frequency_word_counter(data):
    data = data.lower()
    string = data.split()
    dict_string = dict(Counter(string))
    dict_string = list(sorted(dict_string.items(), key=lambda x: (x[1], x[0]), reverse=True))
    maxi = dict_string[0][1]
    l = []
    for i, j in dict_string:
        if j == maxi:
            l.append(i)

    l = sorted(l, key=len, reverse=True)
    word = l[0]
    freq = string.count(l[0])
    print(word, freq)


data = 'Work like you do not need money, love like you have never been hurt, and dance like no one is watching'
max_frequency_word_counter(data)
