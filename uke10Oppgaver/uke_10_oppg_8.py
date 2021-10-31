# prikkprodukt av to lister raise ValueError dersom listene ikke er like lange
def dot_product(a: list, b: list):
    if len(a) != len(b):
        raise ValueError
    zip_a_b = zip(a, b)
    product = 0
    for x, y in zip_a_b:
        product += x * y

    return product

#test
#print(dot_product([1, 2, 3], [2, 3, 5]))
#print(dot_product([1, 2, 3, 4], [2, 3, 5]))
