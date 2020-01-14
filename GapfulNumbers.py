# //A Gapful Number is a number of atleast 3 digits that is divisible by the number formed by the first and last digit of the original number.
# //Sample Input : 192 or 583
# //Output: True (192 is divisible by 12 and 583 is divisible by 53).


def gapful_number(n):
    for i in range(100, n+1):
        res = int(str(i)[0] + str(i)[-1])
        if i % res == 0:
            print("{}".format(i), end=" ")


n = int(input("Enter range :- "))
print("Your Gapful Numbers are :- ")
gapful_number(n)
