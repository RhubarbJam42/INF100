#funksjon som tar liste med positive heltall og returnerer histogram

# Konstruerer et histogram fra verdiene i 'values'.
def render_histogram(values):
    histogram = ''
    width = len(values)
    height = max(values)
    for i in range(height):
        for j in range(width):
            if values[j] == height - i or values[j] > height - i:
                histogram += '*'
            else:
                histogram += ' '
        if i == height - 1:
            histogram += ''
        else:
            histogram += '\n'

    return histogram

#for test purposes
#print(render_histogram([5, 4, 2, 7, 0, 3, 10]))