#mean, median og mode funksjoner som skal brukes som import library
def mean(numbers: list):
    added = 0
    for number in numbers:
        added += number
    return added / len(numbers)


def median(numbers: list):
    #en liste har indexer fra 0-lengden av listen. Dermed for jevne lister vil median bli mid + mid - 1
    numbers.sort()
    middle = int(len(numbers)/2)
    if len(numbers) % 2 == 0:
        return (numbers[middle] + numbers[middle - 1])/2
    else:
        return numbers[middle]


def mode(numbers: list):
    numbers_count = {}
    for n in numbers:
        if n not in numbers_count:
            numbers_count.setdefault(n, 1)
        else:
            numbers_count[n] += 1
    n = numbers[0]
    for key in numbers_count:
        if numbers_count.get(key) > numbers_count.get(n):
            n = key
    return n

