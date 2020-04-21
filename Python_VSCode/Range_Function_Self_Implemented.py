import sys


def self_range(start=0, stop=sys.maxsize, step=1):
    if stop == sys.maxsize:
        stop = start
        start = 0
    
    ls = []
    while start < stop:
        ls.append(start)
        start += step

    return ls


print(self_range(5))
print(self_range(4, 20))
print(self_range(4, 20, 3))


# def lim_range(start, stop, step):
#     ls = []
#     while start < stop:
#         ls.append(start)
#         start += step
#     return ls

# arr = list(map(int, input().split()))
# start, stop = arr[0], arr[1]
# if len(arr) == 3:
#     step = arr[2]
# else:
#     step = 1

# print(lim_range(start, stop, step))
