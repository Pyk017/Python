import string
# import itertools

alpha = string.ascii_letters
# letters = dict(zip(alphabets, range(len(alphabets))))
letters = dict (enumerate(alpha))

# print (alpha)
# print (letters)

def c_cipher (msg, encrypt_key):

    encode = {}
    key = (encrypt_key) %  52

    for i in alpha :
        encode.update({i : key})
        key =  (key + 1) % 52

    print('encode :- ',encode)

    new_msg = ""

    for j in msg:
        # print (encode[j])
        # print (letters[encode[j]])
        if j not in ' ':
            new_msg += letters[encode[j]]
        else:
            new_msg += ' '

    return new_msg


message = input("Enter Message to be Encrypted :- ")
encrypt_key = int(input("Enter a Key :- "))

new = c_cipher(message, encrypt_key)

print ("Your Encoded message is :- {}".format(new))
print ("Your Decrypted Message is :- {}".format(c_cipher(new, -1 * encrypt_key)))

