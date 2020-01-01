# Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.
# Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
'''
Sample Input :- AAAABBBBCCCCCCCCA
Output :- 4A4B8C1A
'''

def encode (message):
    if len(message) == 1:
        return str(1) + message
    count = 0
    digit = []
    for i in range(len(message)-1):
        if message[i] != message[i+1]:
            digit.append(count+1)
            digit.append(message[i])
            count = 0
        else:
            count += 1

    digit.append(count+1)
    digit.append(message[i+1])

    return ''.join(list(map(str, digit)))


string = input("Enter String :- ")
print(encode(string))

