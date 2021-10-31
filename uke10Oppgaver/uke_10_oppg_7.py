#egen get() funksjon
#dicti = {1: 'fuck', 2: 'trap', 6: 'peen'}
def my_get(d, k, v):
    try:
        return d[k]
    except KeyError:
        return v


#test
#print(my_get(dicti, 4, '1'))