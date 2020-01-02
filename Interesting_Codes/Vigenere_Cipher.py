import itertools


def create_key (message, keyword):
    l = list(zip(itertools.cycle(keyword), range(len(message))))
    return [i for i, j in l]


def encrypter (message, key, flag):
    new_str = []
    for i in range(len(message)):
        if flag:
            x = (ord(message[i]) + ord(key[i])) % 26

        else:
            print(ord(message[i]), ord(key[i]))
            x = (ord(message[i]) - ord(key[i]) + 26) % 26

        x +=  ord('a')
        new_str.append(chr(x))

    return ''.join(new_str)


message = input("Enter your String :- ")
keyword = input("Enter your Keyword :- ")
key = create_key(message, keyword)
encrypt = encrypter(message, key, True)
print ("Your encrypted data is :- ", encrypt)
print ("Your Decrypted data is :- ", encrypter(encrypt.upper(), key, False))