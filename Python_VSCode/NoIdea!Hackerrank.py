def happy(n_arr,a_arr,b_arr):
    count = 0
    for i in n_arr:
        if i in a_arr:
            count += 1
        elif i in b_arr:
            count -= 1
        else:
            pass

    return count

inx = input()
n_array = input()
a_array = input()
b_array = input()
o = inx.index(" ")
n = int(inx[:o])
m = int(inx[o+1:])
o = 0
n_arr = n_array.split(" ")
for i in range(n):
    n_arr[i] = int(n_arr[i])

a_arr = a_array.split(" ")
# print(a_arr)
for i in range(m):
    a_arr[i] = int(a_arr[i])

b_arr = b_array.split(" ")
for i in range(m):
    b_arr[i] = int(b_arr[i])

result = happy(n_arr,a_arr,b_arr)
print(result)
# print(n_arr)
# print(n)
# print(m)
# print(a_arr)
# print(b_arr)