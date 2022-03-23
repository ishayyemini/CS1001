# Skeleton file for HW2 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw2_ID.py).

import random

import math


##############
# QUESTION 1 #
##############
#  Q1a


def divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]


#  Q1b
def perfect_numbers(n):
    output = []
    i = 1
    while len(output) < n:
        if i == sum(divisors(i)):
            output.append(i)
        i += 1
    return output


#  Q1c
def abundant_density(n):
    abundant = 0
    for i in range(1, n + 1):
        div_sum = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                div_sum += j
            if div_sum > i:  # we can stop the loop if it's already bigger
                abundant += 1
                break
    return abundant / n


def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    if len(iterable) < r:
        return
    indices = list(range(r))
    yield tuple(iterable[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + len(iterable) - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(iterable[i] for i in indices)


def my_combinations(iterable):
    output = []
    indices = list(range(4))

    print(len(iterable), iterable)

    output = [tuple(iterable[x] for x in indices)]
    for i in reversed(range(4)):
        for j in range(len(iterable) - 4):
            indices[i] += 1
            output.append(tuple(iterable[x] for x in indices))

    # print("should be: ", math.comb(len(iterable), 4), "is: ", len(output))

    return output


print(list(sorted(set([x for x in combinations(divisors(60), 4)]))))
print(my_combinations(divisors(60)))

#  Q1e
def semi_perfect_4(n):
    result = False
    divs = divisors(n)
    if n > sum(divs[-4:]):
        return False

    output = []
    indices = list(range(4))

    output = [sum(divs[x] for x in indices)]
    for i in reversed(range(4)):
        for j in range(len(divs) - 4):
            indices[i] += 1
            output.append(sum(divs[x] for x in indices))

    return output


##############
# QUESTION 2 #
##############
# Q2a
def coin():
    return random.random() >= 0.5


# Q2b
def roll_dice(d):
    return math.ceil(random.random() * d)


# Q2c
def roulette(bet_size, parity):
    gains = 0
    dice = roll_dice(37) - 1
    desired = 0 if parity == "even" else 1

    if dice != 0 and dice % 2 == desired:
        gains = 2

    return bet_size * gains


# Q2d
def roulette_repeat(bet_size, n):
    money = bet_size
    for _ in n:
        money += roulette(bet_size, "even" if coin() else "odd") - bet_size
    return money


print(roulette_repeat(60, 10))

# Q2e
def shuffle_list(lst):
    pass  # replace with your code


##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    pass  # replace with your code


# Q3b
def pad_rev_lists(bin1, bin2):
    pass  # replace with your code


def add(bin1, bin2):
    pass  # replace with your code


# Q3c
def pow_two(binary, power):
    pass  # replace with your code


# Q3d
def div_two(binary, power):
    pass  # replace with your code


# Q3e
def leq(bin1, bin2):
    pass  # replace with your code


# Q3f
def to_decimal(binary):
    pass  # replace with your code


##############
# QUESTION 4 #
##############
# Q4a
def lychrel_loops(n):
    pass  # replace with your code


# Q4b
def is_lychrel_suspect(n, t):
    pass  # replace with your code


# Q4c
def lychrel_sort(numbers, t):
    pass  # replace with your code


##############
# QUESTION 5 #
##############
# Q5a
def calculate_grades_v1(grades):
    pass  # replace with your code


# Q5b
def calculate_grades_v2(grades, w, f):
    pass  # replace with your code


# Q5c_i
def calculate_grades_v3(grades, w):
    pass  # replace with your code


# Q5c_ii
def calculate_w(grades, target_average):
    pass  # replace with your code


##########
# Tester #
##########


def test():
    if divisors(6) != [1, 2, 3] or divisors(7) != [1]:
        print("Error in Q1a")

    if perfect_numbers(2) != [6, 28]:
        print("Error in Q1b")

    if abundant_density(20) != 0.15:
        print("Error in Q1c")

    if not semi_perfect_4(20) or semi_perfect_4(28):
        print("Error in Q1e")

    for i in range(10):
        if coin() not in {True, False}:
            print("Error in Q2a")
            break

    for i in range(10):
        if roll_dice(6) not in {1, 2, 3, 4, 5, 6}:
            print("Error in Q2b")
            break

    for i in range(10):
        if (roulette(100, "even") not in {0, 200}) or (
            roulette(100, "odd") not in {0, 200}
        ):
            print("Error in Q2c")
            break

    shuffled_list = shuffle_list([1, 2, 3, 4])
    for i in range(1, 5):
        if i not in shuffled_list:
            print("Error in Q2e")
            break

    if (
        inc("0") != "1"
        or inc("1") != "10"
        or inc("101") != "110"
        or inc("111") != "1000"
        or inc(inc("111")) != "1001"
    ):
        print("Error in Q3a")

    if (
        add("0", "1") != "1"
        or add("1", "1") != "10"
        or add("110", "11") != "1001"
        or add("111", "111") != "1110"
    ):
        print("Error in Q3b")

    if (
        pow_two("10", 2) != "1000"
        or pow_two("111", 3) != "111000"
        or pow_two("101", 1) != "1010"
    ):
        print("Error in Q3c")

    if (
        div_two("10", 1) != "1"
        or div_two("101", 1) != "10"
        or div_two("1010", 2) != "10"
        or div_two("101010", 3) != "101"
    ):
        print("Error in Q3d")

    if not leq("1010", "1010") or leq("1010", "0") or leq("1011", "1010"):
        print("Error in Q3e")

    if lychrel_loops(28) != 2 or lychrel_loops(110) != 1:
        print("Error in Q4a")

    if (
        (not is_lychrel_suspect(28, 1))
        or is_lychrel_suspect(28, 2)
        or is_lychrel_suspect(28, 3)
    ):
        print("Error in Q4b")

    if lychrel_sort([165, 164, 28, 110, 196], 8) != [110, 28, 165, 164, 196]:
        print("Error in Q4c")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    if calculate_grades_v1(grades) != [95, 90.4]:
        print("Error in Q5a")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    f = lambda x: min(100, x + 3)
    if calculate_grades_v2(grades, w, f) != [95.6, 93.3]:
        print("Error in Q5b")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    w = 0.7
    if calculate_grades_v3(grades, w) != [94.25, 91.8]:
        print("Error in Q5c_i")

    grades = [(95, (85, 90, 95)), (90, (90, 92, 100))]
    target_average = 93.025  # This is the average of [94.25, 91.8]
    if abs(calculate_w(grades, target_average) - 0.7) > 0.000001:
        print("Error in Q5c_ii")
