a = input("Enter a String ")
if len(a) < 3 :
    print ("Useless String")
else :
    if a[-3:] == "ing" :
        a += 'ly'
    else:
        a += 'ing'
    print ("Your new string is {}".format(a))
