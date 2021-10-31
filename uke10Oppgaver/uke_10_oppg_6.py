#trygt legge sammen inputter
def add_together(x, y, z, w):
    return x + y + z + w


def add_together_safely(a, b, c, d):
    try:
        return add_together(a, b, c, d)
    except TypeError as err:
        print(f'Failed with error: {err}')
        return None


#test
#print(add_together_safely(1, 2, 4, 5))
#print(add_together_safely(1, 1, 5, '5'))