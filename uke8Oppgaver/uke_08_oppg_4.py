# lage et program som etterligner gammel egyptisk multiplikasjon for positive heltall som kun fungerer med addisjon og
# fordobling
from copy import copy

a = int(input('Factor A: '))
b = int(input('Factor B: '))


def egyptian_method(factor_a, factor_b):
    a_list = []
    b_list = []
    x_list = []
    index_list = []
    factors = tuple([factor_a, factor_b])

    if factor_a > factor_b:
        factor_b = copy(factors[0])
        factor_a = copy(factors[1])

    #til loopen
    c = copy(factor_b)

    # dobler 1 til tallet under maks og lager en liste
    n = 1
    while n < factor_a:
        a_list.append(n)
        n *= 2
    #dersom factor_a/factor_b < 3
    if n == 2 and factor_a != 1:
        a_list.append(n)
    elif n == 1:
        a_list.append(n)

    # lager en liste som dobler b for hver gang og er på størrelse med a
    for i in range(len(a_list)):
        b_list.append(c)
        c *= 2

    a_max = max(a_list)
    reverse_a = copy(a_list)
    reverse_a.reverse()

    #markerer med de tallene som skal adderes med en X
    for number in reverse_a:
        if number == a_max:
            x_list.append('X')
        elif a_max + number <= factor_a:
            x_list.append('X')
            a_max += number
        else:
            x_list.append(' ')
    x_list.reverse()

    #finner index til X som sier hvilke tall som skal adderes
    for k, item in enumerate(x_list):
        if item == 'X':
            index_list.append(k)

    #til formatering
    line_split = '=' * 25

    #for-loop som legger til i string
    x_marks = ''
    for index in range(len(x_list)):
        spaces_a = ' ' * (3 - len(str(a_list[index])))
        spaces_b = ' ' * (3 - len(str(b_list[index])))
        x_marks += f'{x_list[index]} {spaces_a} {a_list[index]} {spaces_b} {b_list[index]}\n'

    #addisjon av faktor a
    output_add_a = ''
    for x in index_list:
        if x == max(index_list):
            output_add_a += f'{a_list[x]} = {factor_a}'
        elif x == index_list[0]:
            output_add_a += f'{a_list[x]} + '
        else:
            output_add_a += f'{a_list[x]} + '

    #addisjon av faktor b (er a * b, siden addisjonen vil resultere i dette uansett og det gjør det litt lettere)
    output_add_b = ''
    for y in index_list:
        if y == max(index_list):
            output_add_b += f'{b_list[y]} = {factor_a * factor_b}'
        elif y == index_list[0]:
            output_add_b += f'{b_list[y]} + '
        else:
            output_add_b += f'{b_list[y]} + '

    #legger alt sammen tilen string
    output_x = line_split + '\n' + x_marks + line_split + '\n'
    output_addition = output_add_a + '\n' + output_add_b + '\n' + line_split + '\n'
    multiplication = f'{a} * {b} = {a * b}'
    output = output_x + output_addition + multiplication

    return output


print(egyptian_method(a, b))
