# vektproblem med input()
weightByStones = input('Vekt i stones: ')
weightByPounds = input('Vekt i pounds: ')
weightByKg = (float(weightByStones)/0.15747) + (float(weightByPounds)/2.20462)
print('Vekt i kilogram:', weightByKg)

