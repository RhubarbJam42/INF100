# Euler 17

words = {
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
    sn = str(number)
    if number == 1000:
        name += f"one {words.get(number)}"
    elif number == 100:
        name += f"one {words.get(number)}"
    elif number <= 20:
        name += f'{words.get(number)}'
    elif len(sn) == 3:
        if sn[1:] == '00':
            name += f'{words.get(int(sn[0]))} hundred'
        elif sn[2] == '0':
            name += f'{words.get(int(sn[0]))} hundred and {words.get(int(sn[1]) * 10)}'
        elif int(sn[1:]) in words:
            name += f'{words.get(int(sn[0]))} hundred and {words.get(int(sn[1:]))}'
        else:
            name += f'{words.get(int(sn[0]))} hundred and {words.get(int(sn[1]) * 10)}-{words.get(int(sn[2]))}'
    elif len(sn) == 2:
        if sn[1] == '0':
            name += f'{words.get(int(sn[0]) * 10)}'
        else:
            name += f'{words.get(int(sn[0]) * 10)}-{words.get(int(sn[1]))}'
    return name


#kopi fordi lazy
def num_name(number):
    name = ''
    sn = str(number)
    if number == 1000:
        name += f"one{words.get(number)}"
    elif number == 100:
        name += f"one{words.get(number)}"
    elif number <= 20:
        name += f'{words.get(number)}'
    elif len(sn) == 3:
        if sn[1:] == '00':
            name += f'{words.get(int(sn[0]))}hundred'
        elif sn[2] == '0':
            name += f'{words.get(int(sn[0]))}hundredand{words.get(int(sn[1]) * 10)}'
        elif int(sn[1:]) in words:
            name += f'{words.get(int(sn[0]))}hundredand{words.get(int(sn[1:]))}'
        else:
            name += f'{words.get(int(sn[0]))}hundredand{words.get(int(sn[1]) * 10)}{words.get(int(sn[2]))}'
    elif len(sn) == 2:
        if sn[1] == '0':
            name += f'{words.get(int(sn[0]) * 10)}'
        else:
            name += f'{words.get(int(sn[0]) * 10)}{words.get(int(sn[1]))}'
    return name


def all_numbernames(number):
    word = ''
    for i in range(1, number+1):
        word += num_name(i)
    return len(word)


def solve_euler_17():
    return all_numbernames(1000)


#test
#n = 52
#print(len(number_name(n)), number_name(n))
#print(all_numbernames(n))
#print(solve_euler_17())
