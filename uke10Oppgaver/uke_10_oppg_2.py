#lagrer linjene med >>> i starten og <<< i slutten av hver linje
def open_file(filename):
    with open(filename, 'r', encoding='utf8') as file:
        lines = [f">>>{line.strip()}<<<\n" for line in file]
        string = ''
        for i in lines:
            string += i
    return string.strip()


#print(open_file('askeladden.txt'))