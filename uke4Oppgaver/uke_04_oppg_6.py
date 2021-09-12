#øk/mink med 2 mellomrom etter hver print av * med while-loop
spaces = 0
while spaces in range(0, 5):
    print(' ' * 2 * spaces + '*')
    spaces = spaces + 1
    if spaces == 5:
        spaces = spaces - 2
        while True:
            print(' ' * 2 * spaces + '*')
            spaces = spaces - 1
            if spaces < 0:
                spaces = -2
                break