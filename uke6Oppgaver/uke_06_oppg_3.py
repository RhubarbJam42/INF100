#DNA-komplementstreng

def complement(dna_sequence):
    complement_sequence = []
    string_list = list(dna_sequence)
    string_list.reverse()
    sequence = ''
    for item in string_list:
        if item == 'A':
            complement_sequence.append('T')
        elif item == 'T':
            complement_sequence.append('A')
        elif item == 'G':
            complement_sequence.append('C')
        elif item == 'C':
            complement_sequence.append('G')

    for bases in complement_sequence:
        sequence += f'{bases}'

    return sequence

#for test purposes
#dna = 'ATAGCAGT'
#print(complement(dna))