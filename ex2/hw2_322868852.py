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


#  Q1e
def semi_perfect_4(n):
    divs = divisors(n)
    if len(divs) < 4:
        return False
    elif len(divs) == 4:
        return sum(divs) == n

    # We can simply check if n/2 is a sum of three divisors:
    # Let's falsely assume that n/2 isn't in the sum. So, the possible sum
    # is at most: sum <= n/3 + n/4 + n/5 + n/6 = (120+90+72+60)n/360 = 0.95n < n,
    # and we got that there is no possible sum. By that same proof, n must
    # be an even number to be semi prefect by the forth order.
    if n % 2 != 0:
        return False
    tmp_divs = [divs[-2]]

    for i in reversed(range(len(divs) - 2)):
        if sum(tmp_divs) + divs[i] <= n / 2:
            tmp_divs.append(divs[i])
        elif len(tmp_divs) == 1:
            # So, we now have one number, let's mark it as "A", and the new
            # number is "B". We also know that A+B > n/2, so we must use "C"
            # (the number immediately after "B"). But do we use A,C or B,C?
            # if n-(B+C) exists in divs, we got a solution
            # else, we adopt A,C and continue
            if int(n / 2 - sum(divs[i - 1 : i + 1])) in divs:
                return True
            else:
                tmp_divs.append(divs[i - 1])
                i -= 1  # Skip the next iteration
        if sum(tmp_divs) == n / 2:
            if len(tmp_divs) == 3:
                return True
            else:
                tmp_divs.pop()
    return False


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
    for _ in range(n):
        money += roulette(bet_size, "even" if coin() else "odd") - bet_size
    return money


# Q2e
def shuffle_list(lst):
    new_lst = []
    n = len(lst)
    for i in range(n):
        new_lst.append(lst.pop(roll_dice(n - i) - 1))
    return new_lst


##############
# QUESTION 3 #
##############
# Q3a
def inc(binary):
    result = ""
    for i in reversed(range(len(binary))):
        if binary[i] == "0":
            result = binary[:i] + "1" + result
            break
        else:
            result = "0" + result
    else:  # run if "for" didn't break, meaning all digits are "1"
        result = "1" + result
    return result


# Q3b
def add(bin1, bin2):
    result = ""
    carry = 0
    for i in range(1, max(len(bin1), len(bin2)) + 1):
        a = bin1[-i] if i <= len(bin1) else "0"
        b = bin2[-i] if i <= len(bin2) else "0"

        ones_cnt = [a, b, carry].count("1")
        result = ("1" if (ones_cnt == 1 or ones_cnt == 3) else "0") + result
        carry = "1" if ones_cnt > 1 else "0"

    if carry == "1":
        result = "1" + result
    return result


# Q3c
def pow_two(binary, power):
    return binary + "0" * power if binary != "0" else binary


# Q3d
def div_two(binary, power):
    return binary[: len(binary) - power] if 0 <= power < len(binary) else "0"


# Q3e
def leq(bin1, bin2):
    return len(bin1) < len(bin2) or (len(bin1) == len(bin2) and bin1 <= bin2)


# Q3f
def to_decimal(binary):
    result = 0
    for i in range(len(binary)):
        if binary[-i - 1] == "1":
            result += 2**i
    return result


##############
# QUESTION 4 #
##############
def lychrel_helper(n, until=-1):
    x = n
    rev = int(str(x)[::-1])
    i = 0
    while (x != rev or i < 1) and (until < 0 or i <= until):
        x += rev
        rev = int(str(x)[::-1])
        i += 1
    return i


# Q4a
def lychrel_loops(n):
    return lychrel_helper(n)


# Q4b
def is_lychrel_suspect(n, t):
    return lychrel_helper(n, t) > t


# Q4c
def lychrel_sort(numbers, t):
    return sorted(numbers, key=lambda x: lychrel_helper(x, t))


##############
# QUESTION 5 #
##############
# Q5a
def calculate_grades_v1(grades):
    output = []
    for student in grades:
        exam = student[0]
        avg_hw = sum(list(student[1])) / 3
        output.append(exam if exam >= avg_hw else exam * 0.9 + avg_hw * 0.1)
    return output


# Q5b
def calculate_grades_v2(grades, w, f):
    output = []
    for student in grades:
        exam = student[0]
        avg_hw = sum(list(student[1])) / 3
        output.append(f(exam) * w + avg_hw * (1 - w))
    return output


# Q5c_i
def calculate_grades_v3(grades, w):
    output = []
    for student in grades:
        exam = student[0]
        avg_hw = sum(sorted(student[1], reverse=True)[:2]) / 2
        output.append(exam * w + avg_hw * (1 - w))
    return output


# Q5c_ii
def calculate_w(grades, target_average):
    n = len(grades)
    exam_sum, hw_avg_sum = 0, 0
    for student in grades:
        exam_sum += student[0]
        hw_avg_sum += sum(sorted(student[1], reverse=True)[:2]) / 2

    if exam_sum == hw_avg_sum:
        w = 1 if exam_sum / n == target_average else -1
    else:
        w = (target_average * n - hw_avg_sum) / (exam_sum - hw_avg_sum)
    return w if 0 <= w <= 1 else None


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
