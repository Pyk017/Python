customer_details = {1001:'John', 1004:'Jill', 1005:'Jill', 1003:'Jack'}
print ("Customer ID       Customer Name")
for x,y in customer_details.items():
    print ("  {}               {}".format(x,y))

print ("The Numbers of Customer are :- {}".format(len(customer_details)))

b = list(customer_details.values())
print ("Sorted Customer Names are :- \n{}".format(sorted(b)))

customer_details.pop(1005)
print ("After Deletion, Updated Dictionary is :- \n {}".format(customer_details))

customer_details[1003] = 'Mary'
print ("After Insertion, Updated Dictionary is :- \n {}".format(customer_details))

if 1002 in customer_details:
    print ("Customer Details of Customer ID 1002 is Present!")

else:
    print ("Customer Details of Customer ID 1002 is not Present!")

