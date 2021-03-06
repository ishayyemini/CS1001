# Skeleton file for HW4 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).


##############
# Question 1 #
##############
# 1b
def change_v2(amount, coins):
    if not coins:
        return []

    def change_v2_insidious(path, opt, used):
        if not opt or sum(path) >= amount:
            if sum(path) == amount:
                used.append(path)
            return used

        if sum(path + [opt[0]]) <= amount:  # Then we can try with this coin
            change_v2_insidious(path + [opt[0]], opt, used)
        return change_v2_insidious(path, opt[1:], used)

    return change_v2_insidious([], coins, [])


# 1c_ii
def winnable_mem(board):
    d = {}
    return winnable_mem_rec(board, d)


def winnable_mem_rec(board, d):
    if sum(board) == 0:
        return True

    m = len(board)

    for i in range(m):
        for j in range(board[i]):
            munched_board = board[0:i] + [min(board[k], j) for k in range(i, m)]

            key = str(munched_board)
            winnable = d.get(key)
            if winnable is None:
                winnable = winnable_mem_rec(munched_board, d)
                d[key] = winnable

            if not winnable:
                return True

    return False


##############
# Question 2 #
##############
# 2a
def legal_path(A, vertices):
    for i in range(len(vertices) - 1):
        if not A[vertices[i]][vertices[i + 1]]:
            return False
    return True


# 2c
def path_v2(A, s, t, k):
    if k == 0:
        return s == t

    if k == 1:
        return A[s][t] == 1

    for i in range(len(A)):
        mid = k // 2
        if path_v2(A, s, i, mid) and path_v2(A, i, t, k - mid):
            return True
    return False


# 2d # Fix this code without deleting any existing code #
def path_v3(A, s, t):
    if s == t:
        return True

    for i in range(len(A)):
        if A[s][i] == 1:
            A[s][i] = 0
            if path_v3(A, i, t):
                return True
    return False


path_v3_a = None
path_v3_b = ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0, 2)
path_v3_c = None
path_v3_d = ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], 0, 2)


##############
# Question 3 #
##############
# 3a
def can_create_once(s, L):
    if len(L) <= 1:
        return (L[0] if L else 0) == abs(s)

    return can_create_once(s - L[0], L[1:]) or can_create_once(s + L[0], L[1:])


# 3b
def can_create_twice(s, L):
    if len(L) <= 1:
        return (L[0] if L else 0) == abs(s)

    return (
        can_create_twice(s, L[1:])
        or can_create_twice(s - L[0], L[1:])
        or can_create_twice(s + L[0], L[1:])
        or can_create_twice(s - (2 * L[0]), L[1:])
        or can_create_twice(s + (2 * L[0]), L[1:])
    )


# 3c
def calc(lst):
    return eval("".join(map(str, lst)))


def valid_braces_placement(s, L):
    if len(L) == 1:
        return L[0] == s

    for i in range(0, len(L) - 2, 2):
        if valid_braces_placement(s, L[0:i] + [calc(L[i : i + 3])] + L[i + 3 :]):
            return True

    return False


##############
# Question 4 #
##############
# 4a
def grid_escape1(B):
    if len(B) == 0 or B[0][0] == 0:
        return False
    if len(B) == len(B[0]) == 1:
        return True

    steps = B[0][0]
    move_up = B[steps:]
    move_left = list(map(lambda row: row[steps:], B)) if len(B[0][steps:]) else []
    return grid_escape1(move_up) or grid_escape1(move_left)


# 4b
def grid_escape2(B):
    n = len(B)

    def explorer(x, y):
        if x == y == n - 1:
            return True
        if not 0 <= x < n or not 0 <= y < n or B[x][y] == 0:
            return False

        steps = B[x][y]
        B[x][y] = 0
        possible = (
            explorer(x + steps, y)
            or explorer(x - steps, y)
            or explorer(x, y + steps)
            or explorer(x, y - steps)
        )
        B[x][y] = steps

        return possible

    return explorer(0, 0)


##########
# Tester #
##########
def test():
    # 1b
    if len(change_v2(5, [1, 2, 3])) != 5:
        print("error in change_v2")

    # 1c
    if winnable_mem([5, 5, 3]) or not winnable_mem([5, 5, 5]):
        print("error in winnable_mem")

    # 2a
    A = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    if (
        not legal_path(A.copy(), [0, 1, 2, 3])
        or not legal_path(A.copy(), [0, 1, 2, 3, 0, 1])
        or legal_path(A.copy(), [1, 2, 3, 4])
    ):
        print("error in legal_path")

    # 2d
    if path_v3_a != None and not path_v3(path_v3_a[0], path_v3_a[1], path_v3_a[2]):
        print("error in path_v3 or with path_v3_a")

    if path_v3_b != None and not path_v3(path_v3_b[0], path_v3_b[1], path_v3_b[2]):
        print("error in path_v3 or with path_v3_b")

    if path_v3_c != None and path_v3(path_v3_c[0], path_v3_c[1], path_v3_c[2]):
        print("error in path_v3 or with path_v3_c")

    if path_v3_d != None and path_v3(path_v3_d[0], path_v3_d[1], path_v3_d[2]):
        print("error in path_v3 or with path_v3_d")

    # 3a
    if (
        not can_create_once(6, [5, 2, 3])
        or not can_create_once(-10, [5, 2, 3])
        or can_create_once(9, [5, 2, 3])
        or can_create_once(7, [5, 2, 3])
    ):
        print("error in can_create_once")
    # 3b
    if (
        not can_create_twice(6, [5, 2, 3])
        or not can_create_twice(9, [5, 2, 3])
        or not can_create_twice(7, [5, 2, 3])
        or can_create_once(19, [5, 2, 3])
    ):
        print("error in can_create_twice")
    # 3c
    L = [6, "-", 4, "*", 2, "+", 3]
    if (
        not valid_braces_placement(10, L.copy())
        or not valid_braces_placement(1, L.copy())
        or valid_braces_placement(5, L.copy())
    ):
        print("error in valid_braces_placement")

    B1 = [[1, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 1, 2]]
    B2 = [[2, 3, 1, 2], [2, 2, 2, 2], [2, 2, 3, 2], [2, 2, 2, 2]]
    B3 = [[2, 1, 2, 1], [1, 2, 1, 1], [2, 2, 2, 2], [4, 4, 4, 4]]

    # 4a
    if not grid_escape1(B1.copy()):
        print("error in grid_escape1 - B1")
    if grid_escape1(B2.copy()):
        print("error in grid_escape1 - B2")
    if grid_escape1(B3.copy()):
        print("error in grid_escape1 - B3")

    # 4b
    if not grid_escape2(B1.copy()):
        print("error in grid_escape2 - B1")
    if not grid_escape2(B2.copy()):
        print("error in grid_escape2 - B2")
    if grid_escape2(B3.copy()):
        print("error in grid_escape2 - B3")
