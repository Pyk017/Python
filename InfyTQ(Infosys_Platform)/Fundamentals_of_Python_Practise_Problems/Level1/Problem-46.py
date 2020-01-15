"""
This problem is a practice for Debugging covered on Day 3

The code is supposed to replace each value in a list with twice the preceding value (and the first value with 0)

What's wrong with the code:
      An input of [1,2,3] should give [0,2,4]
Debug the code to get the expected output.
"""


def double_preceding(values):
    if len(values) > 0:
        previous = values[0]
        values[0] = 0
        for idx in range(1, len(values)):
            temp = values[idx]
            values[idx] = 2 * previous
            previous = temp

    return values


print(double_preceding([1, 2, 3]))
