import re


def max_even_seq(n):
    # Splits input on odd integers, then returns the highest length
    return max([len(even) for even in re.split("[13579]+", str(n))])


########
# Tester


########
def test():
    if max_even_seq(23300247524689) != 4:
        print("error in max_even_seq")
