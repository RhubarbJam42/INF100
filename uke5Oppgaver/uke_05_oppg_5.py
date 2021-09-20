# funksjoner som beregner max, min og absoluttverdi av to tall
def egen_abs(a):
    if a >= 0:
        a = a
    elif a < 0:
        a = (-1) * a
    return a


#print(egen_abs(-83.0))


def egen_max(a, b):
    c = a - b
    c = egen_abs(c)
    return int((a + b + c) / 2)


#print(egen_max(4, 9))


def egen_min(a, b):
    c = a - b
    c = egen_abs(c)
    return int((a + b - c) / 2)


#print(egen_min(4, 9))


def egen_len(string):
    count = 0
    for i in string:
        count = count + 1
    return count


#print(egen_len('fire'))
