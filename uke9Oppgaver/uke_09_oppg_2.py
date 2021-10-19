# første 10 i Collatz-sekvensen
def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def first_ten_collatz(number):
    first_ten_sequence = {}
    i = 1
    while i <= number:
        first_ten_sequence[i] = collatz_sequence(i)
        i += 1
    return first_ten_sequence


print(first_ten_collatz(10))
