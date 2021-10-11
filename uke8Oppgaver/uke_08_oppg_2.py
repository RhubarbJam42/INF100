#
def pearson_corr(x, y):
    sum_dxdy = 0
    '''
    foreløpig overflødig
    
    mean_x = mean_value(x)  # skal jeg ta med disse?
    mean_y = mean_value(y)
    '''

    dx = change(x)
    dy = change(y)

    dx2 = sum(change_to_power(x))
    dy2 = sum(change_to_power(y))

    sqr_dx2dy2 = (dx2 * dy2) ** 0.5

    for i in range(len(x)):
        sum_dxdy += dx[i] * dy[i]

    return sum_dxdy / sqr_dx2dy2


def mean_value(list_of_values):
    sum_of_numbers = 0
    for numbers in list_of_values:
        sum_of_numbers += numbers
    return sum_of_numbers / len(list_of_values)


def change(list_of_values):
    value_change = []
    for i in list_of_values:
        value_change.append((i - mean_value(list_of_values)))
    return value_change


def change_to_power(list_of_values):
    value_change = []
    for i in list_of_values:
        value_change.append((i - mean_value(list_of_values)) ** 2)
    return value_change


'''
test

x1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2_ls = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

print(sum(change_to_power(y2_ls)), sum(change_to_power(x1_ls)))
print(mean_value([1, 4, 5]))
print(change([1, 2, 3]))
print(pearson_corr(x1_ls, y1_ls))
'''
