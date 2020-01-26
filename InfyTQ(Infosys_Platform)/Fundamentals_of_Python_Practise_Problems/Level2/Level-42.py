"""
Write a function maxvalue_in_column(pixel_grid)
that, given a list of lists of integers, creates a list of integers that includes the maximum value found in each column
 of pixel_grid.

You can assume that pixel_grid will always contain at least one row and one column and that the values in pixel_grid
will be between 0 and 255 and that each row will contain the same number of columns.

Here are a few examples. After the following code is executed:
If pixel_grid contains	Col_list will be

Input :
[ [ 4, 2, 3],
[16, 5, 0],
[ 3, 200, 6],
[ 0, 10, 12]]

Output :
[ 16, 200, 12 ]

Input :
[ [ 4 ],
[ 16 ],
[ 3 ],
[ 0 ]]

Output :
[16]

Input :
[ [ 4, 2, 3] ]

Output :
[ 4, 2, 3 ]

Input :
[ [6] ]

Output :
[ 6 ]
"""


def maxvalue_in_column(grid):
    result_list = []
    temp = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[j][i] > temp:
                temp = grid[j][i]

        result_list.append(temp)
        temp = 0

    return result_list


pixel_grid = [[4, 2, 3], [16, 5, 0], [3, 200, 6], [0, 10, 12]]
pixel_grid1 = [[4], [16], [3], [0]]
pixel_grid2 = [[4, 2, 3]]
pixel_grid3 = [[6]]

print("Pixel grid is:")
for k in pixel_grid:
    print(k)
output = maxvalue_in_column(pixel_grid)
print("The maximum values of each column are:", output)
