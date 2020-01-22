"""
Write a python function to identify and return the number name of a given number. The number should be in range 1 to
1000. If the number is invalid, return -1.

Input                               Output
1                                          one
15                                     fifteen
45                                  forty five
125                 one hundred and twenty five
999                 nine hundred and ninety nine
1000                               one thousand
1211                                         -1
"""
unique = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
          11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
          18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70:
          'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 200: 'two hundred', 1000: 'one thousand',
          300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred', 700: 'seven hundred',
          800: 'eight hundred', 900: 'nine hundred'}


def integer_to_english(number):
    if number in unique:
        return unique[number]

    else:
        if len(str(number)) == 2:
            a = (number // 10) * 10
            b = number % 10
            return integer_to_english(a) + " " + integer_to_english(b)

        elif len(str(number)) == 3:
            a = (number // 100) * 100
            b = number % 100
            return integer_to_english(a) + " and " + integer_to_english(b)

        else:
            return -1


num = int(input())
res = integer_to_english(num)
print(res)
