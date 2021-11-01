import itertools


# funksjon som returnerer kombinasjoner av kort
# k er antall kort som skal bli brukt, n er total som skal oppnås
def card_combinations(k, n):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    all_combinations = []
    combinations = []
    for i in itertools.combinations(cards, k):
        all_combinations.append(i)
    for j in all_combinations:
        if tuple(itertools.accumulate(j))[k-1] == n:
            combinations.append(j)
    return combinations

#test
#print(card_combinations(2, 10))
