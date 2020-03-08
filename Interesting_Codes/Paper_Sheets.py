"""
Sam is given a rectangular paper having dimensions h*w, where h is the height and w is the width. Sam wants to fold the
paper so its dimensions are h1*w1 in the minimum number of moves. The paper can only be folded parallel to its edges and
 after folding, the dimensions should be integers.

For example, given h=8 and w=4, fold the paper until it is h1, w1 = 6, 1. First fold along the long edge 6 units from a
side, resulting in a paper that is 6*4. Next, fold along the width 2 units from the 4 unit edge to have 6*2. Fold along
the center of the 2 unit edge to achieve a 6*1 page in three folds.

minMoves has following parameters :
h : an integer that denotes the initial height
w : an integer that denotes the initial width
h1 : an integer that denotes the final height
w1 : an integer that denotes the final width

Constraints :
1 <= h, w, h1, w1 <= 10^15
h1 <= h
w1 <= w

Sample Input :
2
3
2
2

Sample Output :
1

"""


count = 0


def setting(x, y, x1, y1):
    if x // 2 < x1:
        x = x1
    else:
        x = x // 2
    return x, y


def recur(a, b, c, d):
    global count
    if a == c and b == d:
        return count
    else:
        while a != c or b != d:
            if a != c and a - c < b - d:
                a, b = setting(a, b, c, d)
            elif b != d and a - c > b - d:
                b, a = setting(b, a, c, d)
            elif a == c:
                if d < b // 2:
                    b //= 2
                else:
                    b = d
            elif b == d:
                if c < a // 2:
                    a = a // 2
                else:
                    a = c
            count += 1

    return count


h, w = map(int, input().split())
h1, w1, = map(int, input().split())
print(recur(h, w, h1, w1))
