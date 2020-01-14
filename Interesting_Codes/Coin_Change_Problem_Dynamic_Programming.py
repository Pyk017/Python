<<<<<<< HEAD
def coin_change(ar, n):
    m = len(ar)
    table = [0 for _ in range(n+1)]
    table[0] = 1
    for i in range(m):
        for j in range(ar[i], n+1):
            table[j] += table[j - ar[i]]

        print(table)


coins = list(map(int, input('Enter Coins :- ').split()))
num = int(input('Enter Total Sum :- '))
coin_change(coins, num)
=======
def coin_change(ar, n):
    m = len(ar)
    table = [0 for _ in range(n+1)]
    table[0] = 1
    for i in range(m):
        for j in range(ar[i], n+1):
            table[j] += table[j - ar[i]]

        print(table)


coins = list(map(int, input('Enter Coins :- ').split()))
num = int(input('Enter Total Sum :- '))
coin_change(coins, num)
>>>>>>> Python repo committed
