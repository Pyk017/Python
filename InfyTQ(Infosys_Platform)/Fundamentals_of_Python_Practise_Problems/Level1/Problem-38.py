"""
University of Washington CSE140 Mid term 2015

Write a function build_index_grid(rows, columns) that, given a number of rows and columns, creates a list of lists of that shape that includes the 'row,column' of that location.

For example, after the following code is executed: new_index_grid = build_index_grid(4,3)
new_index_grid would contain:
[['0,0', '0,1', '0,2'],
['1,0', '1,1', '1,2'],
['2,0', '2,1', '2,2'],
['3,0', '3,1', '3,2']]
Note that these are strings.

After the following code is executed : small_index_grid = build_new_grid(1, 1)
small_index_grid would contain: [['0, 0']].
"""


def build_index_grid(rows, columns):
    result = [[str(i)+','+str(j) for j in range(columns)] for i in range(rows)]
    return result


row = 4
col = 3
results = build_index_grid(row, col)
print('Rows: ', row, 'Columns: ', col)
print('The Matrix is :- ', results)
for k in results:
    print(k)
