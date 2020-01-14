# Scope Concept
# x = 'global_x'
# def test():
#     y = "local_y"
#     global x 
#     x = "local_x"
#     print(x)
#     print(y)

# print(x)
# test()
# print(x) 

# List Comprehensition Concept
n = [1,2,3,4,5,6,7,8,9,0]
# myList = []
# for  i in n:
#     myList.append((i))
# print(myList)
myList = [i for i in n] #List Comprehensition
print(myList)

myList2 = [i*i for i in n]
print(myList2)

# Using map + lambda function
myList3 = list(map(lambda x: x*2, n))
print(myList3)

#to find all even number in the list to locate in a separate list
myList4 = [i for i in n if i%2 == 0]
print(myList4)

# using filter + lambda 
myList5 = list(filter(lambda x: x%2 != 0, n))
print(myList5)

# Nested Loop Comprehensition
a = 'abcd'
myList6 = []
for i in a:
    for j in range(len(a)):
        myList6.append((j,i))

print(myList6)

#using List Comprehensition
myList7 = [(j, i) for j in range((len(a))) for i in a ]
print(myList7)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heroes)))
print(dict(zip(names, heroes)))

#if excluding Peter
myDict = {name:hero for name,hero in zip(names, heroes) if name not in 'Peter'}
print(myDict)