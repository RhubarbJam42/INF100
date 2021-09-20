#konverteringer av vekt

def stones_to_pounds(stones):
    return stones * 14


def stones_to_kg(stones):
    return stones / 0.15747

#print(stones_to_kg(1))

def pounds_to_kg(pounds):
    return pounds / 2.20462

#print(pounds_to_kg(1))

def imperial_to_metric(stones, pounds):
    weightkg = round(stones_to_kg(stones) + pounds_to_kg(pounds), 2)
    return weightkg


#print(imperial_to_metric(1,1))