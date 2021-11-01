import random
from collections import Counter


def kast_n_2(n: int):
    die_casts = []
    for i in range(1, n+1):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        die_casts.append(dice_one + dice_two)
    return die_casts


def print_histo(xs: list):
    histogram = ''
    result_count = Counter()
    xs.sort()
    total = 0
    for r in xs:
        result_count[r] += 1
    result_count = dict(result_count)

    for key in result_count:
        total += result_count.get(key)

    for key in result_count:
        stars = (result_count.get(key) / total) * 100 #gir prosent
        histogram += f'{key: 3} {"*" * int(stars)}\n'
    histogram.strip()
    return print(histogram)


#print_histo(kast_n_2(1000))
#print_histo([2, 2, 2, 3, 3, 3, 4, 4, 4])
