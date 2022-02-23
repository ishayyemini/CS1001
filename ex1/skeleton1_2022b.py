# Skeleton file for HW1 - Spring 2022 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.
# you can add new functions if needed.

# Change the name of the file to include your ID number (hw1_ID.py).


# Question 4a
def replace(text, alphabet, new_alphabet):
    output = ""
    for ch in text:
        index = alphabet.find(ch)
        if index >= 0:
            output += new_alphabet[index]
        else:
            output += ch
    return output


# Question 4b
def is_pal(text):
    stripped = text.replace(".", "").replace(" ", "")
    rev = stripped[::-1]
    return stripped == rev


# Question 4c
def num_different_letters(text):
    chars = "abcdefghijklmnopqrstuvwxyz"
    for ch in text:
        if ch in chars:
            chars = chars.replace(ch, "")
    return 26 - len(chars)


# Question 4d
def most_frequent(text):
    counter = {}
    freq = text[0]
    for ch in text:
        if ch in counter.keys():
            counter[ch] += 1
        else:
            counter[ch] = 1
        if counter[ch] > counter[freq]:
            freq = ch
    return freq


# Question 4e
def kth_order(text, k):
    counter = {}
    for ch in text:
        if ch in counter.keys():
            counter[ch] += 1
        else:
            counter[ch] = 1
    after_sort = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return after_sort[k - 1][0]


# Question 5
def calc(expression):
    pass


########
# Tester
########


def test():
    # testing Q4
    if replace("hello world", "abcde fghijkl", "1234567890xyz") != "95zzo6worz4":
        print("error in replace - 1")
    if replace("abcd123", "1", "x") != "abcdx23":
        print("error in replace - 2")

    if not is_pal("go dog"):
        print("error in is_pal - 1")
    if is_pal("anda"):
        print("error in is_pal - 2")

    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")
    if num_different_letters("aaa98765432100000000") != 1:
        print("error in num_different_letters - 2")

    if most_frequent("abcdee") != "e":
        print("error in most_frequent - 1")
    if most_frequent("x11x22x33x") != "x":
        print("error in most_frequent - 2")

    if kth_order("aaaabbbccd", 3) != "c":
        print("error in kth_order - 1")
    if kth_order("abcdabcaba", 1) != "a":
        print("error in kth_order - 2")

    # testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
    if calc("'hi+fi'*'2'*'2'") != "hi+fihi+fihi+fihi+fi":
        print("error in calc - 3")
    if calc("'a'*'2'+'b'*'2'") != "aabaab":
        print("error in calc - 4")
    if calc("'a'*'2'+'b'*'2'-'b'") != "aaaa":
        print("error in calc - 5")
    if calc("'a'*'2'+'b'*'2'-'c'") != "aabaab":
        print("error in calc - 6")
