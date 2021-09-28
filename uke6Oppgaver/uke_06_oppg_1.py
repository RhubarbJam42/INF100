# funksjoner med lister. print funksjonene er tilstede for testing underveis

def remove_sevens(inserted_list):
    while 7 in inserted_list:
        inserted_list.remove(7)
    return inserted_list


#print(remove_sevens([0, 7, 97, 7, 5, 7, 20, 11]))


def every_other(another_list):
    return another_list[:7][::2]


#print(every_other(["a", 1, "b", "c", 2, 6, "g", 4, "p"]))


# ultra_list because bored of regular names
def reverse(ultra_list):
    return ultra_list[::-1]


#print(reverse([1, 2, 3, 4, 5]))


def double_values(double_list):
    double_list = [item * 2 for item in double_list]
    return double_list


#print(double_values([1, 2, 3, 4]))


def unique_values(special_list):
    unique_list = []
    for item in special_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


#print(unique_values([1, 5, 2, 1, 2, 2, 5, 6, 0, 2]))