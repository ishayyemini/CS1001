# Skeleton file for HW4 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).
import math


##############
# Question 1 #
##############
# 1b
def change_v2(amount, coins):
    pass  # replace with your code


# 1c_ii
def winnable_mem(board):
    d = {}
    return winnable_mem_rec(board, d)


def winnable_mem_rec(board, d):
    pass  # replace this with your code


##############
# Question 2 #
##############
# 2a
def legal_path(A, vertices):  # noqa
    for i in range(len(vertices) - 1):
        if not A[vertices[i]][vertices[i + 1]]:
            return False
    return True


# 2c
def path_v2(A, s, t, k):  # noqa
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
def path_v3(A, s, t):  # noqa
    if s == t:
        return True

    for i in range(len(A)):
        if A[s][i] == 1:
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
    pass  # replace this with your code


# 3b
def can_create_twice(s, L):
    pass  # replace this with your code


# 3c
def valid_braces_placement(s, L):
    pass  # replace this with your code


##############
# Question 4 #
##############
# 4a
def grid_escape1(B):
    pass  # replace this with your code


# 4b
def grid_escape2(B):
    pass  # replace this with your code


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
