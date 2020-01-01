def find_correct(word):
    l = [0]*3
    if len(word) == 1:
        l[2] = 1
        return l

    count = 0
    for i, j in word.items():
        if i in j:
            l[0] += 1
        elif len(i) != len(j):
            l[2] += 1
        else:
            l2 = list(zip(i, j))
            for k, m in l2:
                if k != m:
                    count += 1

            if count <= 2:
                l[1] += 1
            else:
                l[2] += 1
            count = 0

    return l


word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS", "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
