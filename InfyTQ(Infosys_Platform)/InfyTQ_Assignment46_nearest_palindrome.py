def nearest_palindrome(num):
    while True:
        num += 1
        if str(num) in str(num)[::-1]:
            break

    return int(num)


n = int(input("Enter a Number :- "))
print("Nearest Palindrome of your number is :- ",nearest_palindrome(n))
