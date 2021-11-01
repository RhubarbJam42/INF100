from datetime import date

# telle antall onsdager som havner på den første i hver måned i året fra 1901-2000
wednesday = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        # trenger kun å se på den første i hver måned. .weekday() == 3 tilsvarer onsdag
        if date(y, m, 1).weekday() == 2:
            wednesday += 1
print(wednesday)

