#lager en ny tekst-fil med temperaturer
def r_w_file(infile, outfile):
    with open(infile, 'r', encoding='utf8') as file:
        to_write = ''
        for line in file:
            day, temp = line.split()
            if float(temp) >= 23.5:
                to_write += f'{day} {temp}\n'
        file.close()
    with open(outfile, 'w', encoding='utf8') as o_file:
        o_file.write(to_write.strip())
    return None #om den i det hele tatt skal returnere noe?


#test
#r_w_file('temperatures.txt', 'new_temperatures.txt')