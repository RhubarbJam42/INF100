#change machine: funksjon som regner ut vekslepenger

def return_change(payment, price):
    change_back = []
    coins = (20, 10, 5, 1)
    #int fordi mynter kan ikke bli delt inn i desimaler
    change = int(payment) - int(price)

    #Andre versjon av koden
    for coin in coins:
        while change >= coin:
            change_back.append(coin)
            change -= coin

    ''' Første versjon av koden. Med denne måten må man også reversere listen
    while change > 0:
        if change % 20 == 0:
            change_back.append(20)
            change -= 20
        elif change % 10 == 0:
            change_back.append(10)
            change -= 10
        elif change % 5 == 0:
            change_back.append(5)
            change -= 5
        elif change % 1 == 0:
            change_back.append(1)
            change -= 1'''
    return change_back

#test
#print(return_change(134, 25))