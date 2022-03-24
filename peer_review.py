import re
from timeit import timeit

from simple_colors import *


def max_even_seq_mine(n):
    # Splits input on odd integers, then returns the highest length
    return max([len(even) for even in re.split("[13579]+", str(n))])


def max_even_seq_21632(n):
    cnt = 0
    cnt_max = 0
    while n > 0:
        if n % 2 == 0:
            cnt += 1
            n = n // 10
            if cnt > cnt_max:
                cnt_max = cnt
        else:
            cnt = 0
            n = n // 10
    return cnt_max


def max_even_seq_81523(n):
    if n == 0:
        return 1
    cnt = 0
    cnt_max = 0
    num = str(n)
    for i in num:
        if int(i) % 2 == 0:
            cnt += 1
        else:
            if cnt > cnt_max:
                cnt_max = cnt
                cnt = 0
    return cnt_max


def max_even_seq_77528(n):
    max = 0
    temp = 0
    for i in str(n):
        i = int(i)
        if i % 2 == 0:
            temp += 1
            if temp > max:
                max = temp
        else:
            temp = 0
    return max


q1_inputs = (3, 0, 50505050555555500000, 12212)
q1_expected = (0, 1, 5, 2)

q2_powers = (20, 500, 1000, 5000)


for func in [max_even_seq_21632, max_even_seq_81523, max_even_seq_77528]:
    print("\033[1m" + func.__name__ + "\033[0m")

    print("Testing Q1")
    for x in range(4):
        res = func(q1_inputs[x])
        sign = "  ✌️" if res == q1_expected[x] else "  💀"
        print(
            sign,
            "Input: " + str(q1_inputs[x]),
            "Expected: " + blue(q1_expected[x]),
            "Got: " + (green(res) if res == q1_expected[x] else red(res)),
        )

    print("Testing Q2")
    for x in range(4):
        actual_time = timeit(lambda: func(2 ** q2_powers[x]), number=10000)
        expected_time = timeit(
            lambda: max_even_seq_mine(2 ** q2_powers[x]), number=10000
        )
        sign = "  ✌️" if actual_time <= expected_time else "  💀"
        print(
            sign,
            "Input: 2**" + str(q2_powers[x]),
            "Expected Time: " + blue(expected_time),
            "Actual Time: "
            + (
                green(actual_time) if actual_time <= expected_time else red(actual_time)
            ),
        )

    print()
