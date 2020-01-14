'''
Program to build a student database to enter student details and calculate average of students marks and set all
details of student in the dictionary of all student. When user enters the ID the a Student , program will show all the
details of that particular student.
'''
def average (a,b,c,d):
    return (a+b+c+d)/4

n = int(input("Enter number of Students :- "))
l = [{} for i in range(n)]
dic = {}
for i in range(0,n):
    dic["name"] = input("Enter the Name of Student No. {} :- ".format(i+1))
    dic["id"] = int(input("Enter the ID of Student No. {} :- ".format(i+1)))
    dic["branch"] = input("Enter the Branch of Student No. {} :- ".format(i+1))
    dic["mark1"] = int((input("Enter Mark1 of Student No. {} :- ".format(i+1))))
    dic["mark2"] = int((input("Enter Mark2 of Student No. {} :- ".format(i + 1))))
    dic["mark3"] = int((input("Enter Mark3 of Student No. {} :-  ".format(i + 1))))
    dic["mark4"] = int((input("Enter Mark4 of Student No. {} :- ".format(i + 1))))
    dic["avg"] = average(dic["mark1"],dic["mark2"],dic["mark3"],dic["mark4"])
    l[i] = dic
    dic = {}

t,flag = 1,0
while t:
    idi = int(input("Enter ID of Student to be Searched :- "))
    for i in l:
        if idi == i.get("id"):
            print("Name = {}\nCollege ID = {}\nBranch = {}\nMarks of Subject01 = {}\nMarks of Subject02 = {}\nMarks of Subject03 = {}\nMarks of Subject04 = {}\n Average :- {}".format(i["name"],i["id"],i["branch"],i["mark1"],i["mark2"],i["mark3"],i["mark4"],i["avg"]))
            flag = 1
            break

    if flag is 0:
        print ("Data not Found!")

    t = int(input("Do you want to Search any Student by ID , if YEs Press 1 or Press 0 to exit!"))
    flag = 0



