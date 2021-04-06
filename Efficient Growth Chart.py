##
##=======================================================
## Jaskirat Pabla
## Efficient Growth Chart
##=======================================================
##


import check


## Data Definition:

## A GrowthChart, GC, is a (listof (list of Str))
## Requires:
##     The length of the outer list and each inner list is the same
##     (and positive).
##     Each string is '.' or 'X'.
##     For each column c, there is a row r such that 0 <= r < n,
##         GC[i][c] = '.' for 0 <= i < r, and
##         GC[i][c] = 'X' for r <= i < n.
##     For each row r, GC[r] = ['.']*s + ['X']*t where 0 <= s,t < n


## Constant for Testing:
sample_chart = [['.','.','.','.','.','.','X','X'],
                ['.','.','.','.','.','X','X','X'],
                ['.','.','.','.','X','X','X','X'],
                ['.','.','.','X','X','X','X','X'],
                ['.','.','.','X','X','X','X','X'],
                ['.','.','.','X','X','X','X','X'],
                ['.','.','X','X','X','X','X','X'],
                ['X','X','X','X','X','X','X','X']]


def sum_to(GC, threshold):
    '''
    Returns the sum of the heights of each column with
    a height that is less than or equal to threshold in GC.

    sum_to: GrowthChart Nat -> Nat

    Examples:
    sum_to(sample_chart, 0) => 0
    sum_to(sample_chart, 5) => 9
    sum_to(sample_chart, 282312) => 38
    '''
    length = len(GC)
    col = 0
    row = length - 1
    score = 0
    height = 1
    while ((height <= threshold) and (col < length)):
        truth = True
        additional_x = 0
        while (truth != False):
            total_x = height + additional_x
            row -= 1
            if (total_x > threshold):
                additonal_x = 0
                truth = False
            elif (row < 0):
                truth = False
            elif (GC[row][col] != 'X'):
                row += 1
                truth = False
            else:
                additional_x += 1
        height += additional_x
        if (height <= threshold):
            score += height
        col += 1
    return score


## Examples:
check.expect('threshold of 0', sum_to(sample_chart, 0), 0)
check.expect('typical case', sum_to(sample_chart, 5), 9)
check.expect('extremely large threshold',
             sum_to(sample_chart, 282312), 38)


## Tests:
check.expect("n=1, threshold=0", sum_to([['X']], 0), 0)
check.expect("n=1, threshold=1", sum_to([['X']], 1), 1)
check.expect("n=1, threshold>1", sum_to([['X']], 257), 1)
check.expect('threshold of 1', sum_to(sample_chart, 1), 2)
check.expect('threshold of 2', sum_to(sample_chart, 2), 4)
check.expect('threshold that is not the exact height of any column of GC', 
             sum_to(sample_chart, 4), 4)
check.expect('typical case', sum_to(sample_chart, 6), 15)
check.expect('typical case', sum_to(sample_chart, 7), 22)
check.expect('another typical case', sum_to(sample_chart, 8), 38)
check.expect('extremely even larger threshold',
             sum_to(sample_chart, 9999999999999999999999999999), 38)


## Other Tests:
n = 50
stair_case = []
for i in range(n):
 stair_case.append(['.']*(n-i-1)+['X']*(i+1))
check.expect("staircase, threshold=0", sum_to(stair_case,0), 0)
check.expect("staircase, threshold=1", sum_to(stair_case,1), 1)
check.expect("staircase, threshold=25", sum_to(stair_case,25), 25*26//2)
check.expect("staircase, threshold=50", sum_to(stair_case,50), 50*51//2)

low_towers = [['.']*4]*3 + [['X']*4]
check.expect("all towers one 'X', threshold=0", sum_to(low_towers,0), 0)
check.expect("all towers one 'X', threshold=1", sum_to(low_towers,1), 4)
check.expect("all towers one 'X', threshold>1", sum_to(low_towers,116), 4)

full_towers = [['X']*7]*7
check.expect("7 full towers, threshold=0", sum_to(full_towers,0), 0)
check.expect("7 full towers, threshold=3", sum_to(full_towers,3), 0)
check.expect("7 full towers, threshold=7", sum_to(full_towers,7), 49)
check.expect("7 full towers', threshold>7", sum_to(full_towers,116), 49)


## Efciency Tests:
n = 20000

empty_row = ['.']*n
half_row = ['.']*(n//2)
half_row.extend(['X']*(n//2))
full_row = ['X']*n

low_towers = [empty_row]*(n-1)
low_towers.extend([full_row])
check.expect("all towers one 'X', threshold=0", sum_to(low_towers,0), 0)
check.expect("all towers one 'X', threshold=1", sum_to(low_towers,1), n)
check.expect("all towers one 'X', threshold>1", sum_to(low_towers,116), n)

full_towers = [full_row]*n
check.expect("full towers, threshold=0", sum_to(full_towers,0), 0)
check.expect("full towers, threshold=3", sum_to(full_towers,3), 0)
check.expect("full towers, threshold=n", sum_to(full_towers,n), n*n)
check.expect("full towers', threshold>n", sum_to(full_towers,n+1), n*n)

backwardsL = [half_row]*(n//2)
backwardsL.extend([full_row]*(n//2))
check.expect("backwards L, threshold=0", sum_to(backwardsL,0), 0)
check.expect("backwards L, threshold=1", sum_to(backwardsL,1), 0)
check.expect("backwards L, threshold=n//2",
             sum_to(backwardsL,n//2), (n//2)*(n//2))
check.expect("backwards L, threshold=n",
             sum_to(backwardsL,n), (n//2)*(n//2) + (n//2)*(n))
