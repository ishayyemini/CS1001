import time


def zeros1(num):  # 1st solution
    m = num
    cnt = 0
    while m > 0:
        if m % 10 == 0:
            cnt = cnt + 1
        m = m // 10
    return cnt


def zeros2(num):  # 2nd solution
    cnt = 0
    snum = str(num)  # num as a string
    for digit in snum:
        if digit == "0":
            cnt = cnt + 1
    return cnt


def zeros3(num):  # 3rd solution
    cnt = str.count(str(num), "0")
    return cnt


def loop(num):
    cnt = 0
    for i in range(num):
        cnt = cnt + 1
    return cnt


values = [2 ** 100]

index = 1
for zeros in [loop]:
    print('zeros', index)
    for value in values:
        t0 = time.perf_counter_ns()
        zeros(value)
        t1 = time.perf_counter_ns()
        print("Value: ", value)
        print("Amount of zeros: ", zeros(value))
        print("Running time: ", t1 - t0, "nanoseconds")
    print()
    index += 1
