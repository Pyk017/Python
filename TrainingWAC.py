#Program to design a menu driven program for dictionary fetch system and fetching !
dic = {"abase":"cause to feel shame", "aberration":"a state or condition markedly different from the norm", "abhor":"find repugnant", "abstrain":"refrain from doing", "abstract":"existing only in mind", "abundant":"present in great quantity", "accord":"concurrence of opinion"}
t = 1
l = []
flag = 0
while t:
    data = input("Enter word to be searched from the database !")
    for x,y in dic.items():
        if x in data :
            print ("Meaning of your word is :- {}".format(y))
            l.append(x)
            flag = 1

    if flag is 0:
        print("Data not found in the database !\n Do you want to update the Dictionary \n Press 1 to update or 0 to close!")
        choice = int(input())
        if choice is 1:
            meaning = input("Enter Meaning to be updated in the Dictionary.")
            dic[data] = meaning
        else:
            pass

    print ("Want to search more ! ")
    t = int(input("Enter 1 to continue or 0 to stop !"))
    flag = 0

print ("Your Search history is :- {}".format(l))