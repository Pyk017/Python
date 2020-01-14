def validate_credit_card_number(card_number):
    abc = list(map(lambda x: x * 2, list(map(int, card_number[-2::-2]))))
    l = []
    for i in abc:
        if i > 9:
            l.append(sum(list(map(int, str(i)))))
        else:
            l.append(i)

    sumi1 = sum(l)
    sumi = sum(list(map(int, card_number[-1::-2])))

    return True if (sumi + sumi1) % 10 == 0 else False


card_number = input("Enter Card Number :- ") #Sample Inputs :- 1456734512345698 4539869650133101, 1456734512345698, 5239512608615007
result = validate_credit_card_number(card_number)
print("Credit Card Number is Valid!") if result else print("Credit Card Number is not Valid!")
