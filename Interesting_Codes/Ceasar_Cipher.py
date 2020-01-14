import string

alphaLower = string.ascii_lowercase
alphaUpper = string.ascii_uppercase

lettersLower = dict (enumerate(alphaLower))
lettersUpper = dict (enumerate(alphaUpper))

def c_cipher (msg, encrypt_key):

    encodeLower = {}
    encodeUpper = {}

    key = encrypt_key %  26

    for i in alphaLower :
        encodeLower.update({i : key})
        key =  (key + 1) % 26

    key = encrypt_key % 52

    for i in alphaUpper :
        encodeUpper.update({i : key})
        key =  (key + 1) % 26

    print('encodeLower :- ',encodeLower)
    print ('encodeUpper :- ', encodeUpper)

    new_msg = ""

    for j in msg:
        if j in j.lower():
            if j not in ' ':
                new_msg += lettersLower[encodeLower[j]]

            else:
                new_msg += ' '

        else:
            if j not in ' ':
                new_msg += lettersUpper[encodeUpper[j]]

            else:
                new_msg += ' '

    return new_msg


message = input("Enter Message to be Encrypted :- ")
encrypt_key = int(input("Enter a Key :- "))

new = c_cipher(message, encrypt_key)

print ("Your Encrypted message is :- {}".format(new))
print ("Your Decrypted Message is :- {}".format(c_cipher(new, -1 * encrypt_key)))

# =======
import string

alphaLower = string.ascii_lowercase
alphaUpper = string.ascii_uppercase

lettersLower = dict (enumerate(alphaLower))
lettersUpper = dict (enumerate(alphaUpper))

def c_cipher (msg, encrypt_key):

    encodeLower = {}
    encodeUpper = {}

    key = encrypt_key %  26

    for i in alphaLower :
        encodeLower.update({i : key})
        key =  (key + 1) % 26

    key = encrypt_key % 52

    for i in alphaUpper :
        encodeUpper.update({i : key})
        key =  (key + 1) % 26

    print('encodeLower :- ',encodeLower)
    print ('encodeUpper :- ', encodeUpper)

    new_msg = ""

    for j in msg:
        if j in j.lower():
            if j not in ' ':
                new_msg += lettersLower[encodeLower[j]]

            else:
                new_msg += ' '

        else:
            if j not in ' ':
                new_msg += lettersUpper[encodeUpper[j]]

            else:
                new_msg += ' '

    return new_msg


message = input("Enter Message to be Encrypted :- ")
encrypt_key = int(input("Enter a Key :- "))

new = c_cipher(message, encrypt_key)

print ("Your Encrypted message is :- {}".format(new))
print ("Your Decrypted Message is :- {}".format(c_cipher(new, -1 * encrypt_key)))

# >>>>>>> Python repo committed
