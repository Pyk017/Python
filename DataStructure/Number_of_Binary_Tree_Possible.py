import math


def unlabelled(n):
    num, deno = 1, 1
    for i in range(2*n, n, -1):
        num *= i
        deno *= (i - n)

    result = num // (deno * (n + 1))
    return result


def labelled(node):
    return unlabelled(node) * math.factorial(node)


nodes = int(input("Enter total number of nodes :- "))
print("When nodes are found to be UnLabelled :- ", unlabelled(nodes))
print("When nodes are found to be Labelled :- ", labelled(nodes))
