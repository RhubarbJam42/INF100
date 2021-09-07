# Lage et haiku med lengste linje på andre rad?
firstRow = input('Første raden: ')
secondRow = input('Andre raden: ')
thirdRow = input('Tredje raden: ')
lengthFirstRow = len(firstRow)
lengthSecondRow = len(secondRow)
lengthThirdRow = len(thirdRow)
longestRow = max(lengthFirstRow, lengthSecondRow, lengthThirdRow)
print()
print('@' + '@' * (longestRow+2) + '@')
print('@', ' ' * (longestRow - lengthFirstRow) + firstRow, '@')
print('@', ' ' * (longestRow - lengthSecondRow) + secondRow, '@')
print('@', ' ' * (longestRow - lengthThirdRow) + thirdRow, '@')
print('@' + '@' * (longestRow+2) + '@')


