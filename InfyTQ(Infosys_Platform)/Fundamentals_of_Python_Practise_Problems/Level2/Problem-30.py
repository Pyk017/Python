"""
Write a Python function that creates a new text file in which all the lines from the original text file are present and
numbered from 1 to n.(where n is the number of lines in the file.)
"""

with open('practice.txt', 'r') as file1:
    with open('practice_2.txt', 'w') as file2:
        i = 1
        for line in file1:
            file2.write(str(i) + ' ' + line)
            i += 1
