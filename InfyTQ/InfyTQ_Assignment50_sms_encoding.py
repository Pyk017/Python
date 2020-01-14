def sms_encoding(data):
    vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    ls = data.split()
    lss = []
    count = 0
    string = ''
    for i in ls:
        for j in i:
            if j in vowel:
                count += 1
            else:
                string += j

        if count == len(i):
            lss.append(i)

        else:
            lss.append(string)

        count = 0
        string = ''

    return ' '.join(lss)


dataa = input("Enter message to be encoded :- ")
print('Your SMS encoded will be :- ', sms_encoding(dataa))
