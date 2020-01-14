"""
Write a Python function to create and return a new dictionary from the given dictionary(item:price).
Given the following input, create a new dictionary with elements having price more than 200.

Sample Input :
{'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
{'Mango': 150.45, 'Pomegranate': 250.67, 'Banana': 20.55, 'Cherry': 500.10, 'Orange': 200.75}

Sample Output :
{'AAPL': 612.78, 'IBM': 205.55}
{'Orange': 200.75, 'Cherry': 500.10, 'Pomegranate': 250.67}
"""


def new_dictionary(prices):
    new_dict = {i: j for i, j in prices.items() if j > 200}
    return new_dict


dictionary = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
print(new_dictionary(dictionary))
