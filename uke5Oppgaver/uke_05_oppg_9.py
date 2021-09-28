# funciton drawing a frame around a haiku

def draw_haiku_frame(first_row, second_row, third_row):
    length_first_row = len(first_row)
    length_second_row = len(second_row)
    length_third_row = len(third_row)

    longest = max(length_first_row, length_second_row, length_third_row)

    haiku_one = '@' + '@' * (longest + 2) + '@' f'\n'
    haiku_two = '@' + ' ' * (longest - length_first_row + 1) + f'{first_row}' ' ' '@' f'\n'
    haiku_three = '@' + ' ' * (longest - length_second_row + 1) + f'{second_row}' ' ' '@' f'\n'
    haiku_four = '@' + ' ' * (longest - length_third_row + 1) + f'{third_row}' ' ' '@' f'\n'
    haiku_five = '@' + '@' * (longest + 2) + '@'
    haiku = haiku_one + haiku_two + haiku_three + haiku_four + haiku_five
    return haiku



#sjekke funksjonen
#print(draw_haiku_frame('Haruno-umi', 'Hinemosu-Notari', 'Notarikana'))
