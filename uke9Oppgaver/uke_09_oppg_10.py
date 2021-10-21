# Euler 17

numbers_name = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def number_name(number):
    name = ''
    if number == 1000:
        name = "one" + numbers_name.get(1000)
    elif number == 100:
        name = "one" + numbers_name.get(100)
    elif 100 < number < 200:
        name = "one" + numbers_name.get(100) + "and"
        number -= 100
        if number in numbers_name:
            name += numbers_name.get(number)

    return name


# def all_numbernames(N):

# def solve_euler_17():


print(number_name(100))
