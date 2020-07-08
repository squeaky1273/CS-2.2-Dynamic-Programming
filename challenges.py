class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA)
    cols = len(strB)

    dp_table = [[None]*(cols + 1) for i in range(rows + 1)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows + 1):
        for col in range(cols + 1):
            if row == 0 or col == 0:
                dp_table[row][col] = 0
            elif strA[row-1] == strB[col-1]:
                dp_table[row][col] = dp_table[row-1][col-1] + 1
            else:
                dp_table[row][col] = max(dp_table[row-1][col], dp_table[row][col-1])

    return dp_table[rows][cols]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if len(items) == 0 or capacity == 0:
        return 0

    value_without = knapsack(items[1:], capacity)

    if capacity < items[0][1]:
        return value_without
    else:
        value_with = items[0][2] + knapsack(items[1:], capacity - items[0][1])
        return max(value_with, value_without)

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows):
        for col in range(cols):
            if rows == 0 or cols == 0:
                dp_table[row][col] = 0

            elif items[row-1][1] > col:
                dp_table[row][col] = dp_table[row-1][col]

            else:
                value_with = items[row-1][2] + dp_table[row-1][col - items[row-1][1]]
                value_without = dp_table[row-1][col]
                dp_table[row][col] = max(value_with, value_without)

    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2, m, n):
    """Compute the Edit Distance between 2 strings."""
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)

    insert = edit_distance(str1, str2, m, n-1)
    delete = edit_distance(str1, str2, m-1, n)
    replace =  edit_distance(str1, str2, m-1, n-1)

    return 1 + min(insert, delete, replace)

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for row in range(rows):
        dp_table[row][0] = row

    for col in range(cols):
        dp_table[0][col] = col

    for row in range(1,rows):
        for col in range(1,cols):
            if str1[row-1] == str2[col-1]:
                dp_table[row][col] = dp_table[row-1][col-1]
            else:
                insert = dp_table[row][col-1]
                delete = dp_table[row-1][col]
                replace = dp_table[row-1][col-1]
                dp_table[row][col] = min(insert, delete, replace) + 1

    return dp_table[rows-1][cols-1]