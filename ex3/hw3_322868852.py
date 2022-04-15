# Skeleton file for HW3 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).
import math
import random

# Q2 - C
def oct_to_fraction(octal):
    pass  # replace this with your code


# Q2 - D
oct_to_float = lambda octal: None  # replace None with your code


# Q2 - E
def is_greater_equal(oct1, oct2):
    pass  # replace this with your code


# Q3 - A
def approx_root(x, eps):
    sequence = []
    seq_sum = 0
    last_elem = 1  # Last element in the shape of 1/(a1*...*an)
    offset = 0  # Difference between last int in sequence and the next one to check

    while (seq_sum + eps) ** 2 <= x:
        try_int = (sequence[-1] if len(sequence) else 1) + offset
        try_elem = last_elem * (1 / try_int)

        if (seq_sum + try_elem) ** 2 <= x:
            last_elem = try_elem
            sequence.append(try_int)
            seq_sum += last_elem
            offset = 0
        else:
            offset += 1

    return sequence, seq_sum


# Q3 - B
def almost_one():
    total = 0
    rounds = 0
    while total < 1:
        total += random.random()
        rounds += 1
    return rounds


def approx_e(N):
    return sum(almost_one() for _ in range(N)) / N


# Q4 - A
def find(lst, s):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if s == lst[mid]:
            return mid
        elif s < lst[mid]:  # Item cannot be above mid+1 as the list is almost sorted
            if mid < right and s == lst[mid + 1]:
                return mid + 1
            right = mid - 1
        else:
            if mid > left and s == lst[mid - 1]:
                return mid - 1
            left = mid + 1

    return None


# Q4 - B
def sort_from_almost(lst):
    i = 0
    while i < (len(lst) - 1):
        item = lst[i]
        next_item = lst[i + 1]
        if item > next_item:
            lst[i] = next_item
            lst[i + 1] = item
            i += 1  # We can skip checking the next item as we just set it
        i += 1
    return lst


# Q4 - C
def generate_queries(k=100, n=1000):
    L = []
    for i in range(n):
        L.append(random.randint(0, k - 1))

    def q_g(m):
        size = 0
        for i in range(n):
            if L[i] > m:
                size += 1
        return size

    def q_l(m):
        size = 0
        for i in range(n):
            if L[i] < m:
                size += 1
        return size

    return q_l, q_g


k = 100000
n = 100
q_l, q_g = generate_queries(k, n)


def compute_median(q_l, q_g, k, n):
    pass  # replace this with your code


# Q5 - A
def string_to_int(s):
    pass  # replace this with your code


# Q5 - B
def int_to_string(k, n):
    pass  # replace this with your code


# Q5 - C
def sort_strings1(lst, k):
    pass  # replace this with your code


# Q5 - E
def sort_strings2(lst, k):
    pass  # replace this with your code


##########
# Tester #
##########
def test():
    # Q2 - C
    if (
        oct_to_fraction("621000000000") != 0.783203125
        or oct_to_fraction("202200000000") != 0.25439453125
    ):
        print("error in oct_to_fraction")
    # Q2 - D
    if oct_to_float("0400621000000000") != 51.859375:
        print("error in oct_to_float")
    # Q2 - E
    if (
        is_greater_equal("0401010000000000", "0400010000000000") == False
        or is_greater_equal("0400007777777777", "0400010000000000") == True
    ):
        print("error in is_greater_equal")
    # Q3 - A
    if approx_root(2, 0.1) != ([1, 3], 1 + 1 / 3):
        print("error in approx_root (1)")
    if approx_root(2, 0.02) != ([1, 3, 5], 1 + 1 / 3 + 1 / 15):
        print("error in approx_root (2)")
    if approx_root(2, 0.001) != ([1, 3, 5, 5], 1 + 1 / 3 + 1 / 15 + 1 / 75):
        print("error in approx_root (3)")
    # Q3 - B
    if abs(approx_e(1000000) - math.e) > 0.01:
        print("MOST LIKELY there's an error in approx_e (this is a probabilistic test)")

    # Q4 - A
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]
    if find(almost_sorted_lst, 5) != 3:
        print("error in find")
    if find(almost_sorted_lst, 50) != None:
        print("error in find")

    # Q4 - B
    if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        print("error in sort_from_almost")

    # Q4 - C
    M = compute_median(q_l, q_g, k, n)
    if not ((q_l(M) <= n // 2) and (q_g(M) <= n // 2)):
        print("error in compute_median")

    # Q5
    lst_num = [random.choice(range(5**4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if string_to_int(s) != i:
            print("error in int_to_string and/or in string_to_int")

    lst1 = [
        "aede",
        "adae",
        "dded",
        "deea",
        "cccc",
        "aacc",
        "edea",
        "becb",
        "daea",
        "ccea",
    ]
    if sort_strings1(lst1, 4) != [
        "aacc",
        "adae",
        "aede",
        "becb",
        "cccc",
        "ccea",
        "daea",
        "dded",
        "deea",
        "edea",
    ]:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) != [
        "aacc",
        "adae",
        "aede",
        "becb",
        "cccc",
        "ccea",
        "daea",
        "dded",
        "deea",
        "edea",
    ]:
        print("error in sort_strings2")
