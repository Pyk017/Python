"""
Write a python function which accepts any number in the range of 1 to 4999 (both inclusive) and returns the equivalent
roman numeral of it.

Sample input	Expected output
1	                I
1796	        MDCCXCVI
4998	        MMMMCMXCVIII
"""


def convert_to_roman(num):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []
    for i in range(len(ints)):
        count = int(num / ints[i])
        result.append(nums[i] * count)
        num -= ints[i] * count
    return ''.join(result)


for j in range(1, 5000):
    print(j, " : ", convert_to_roman(j))
