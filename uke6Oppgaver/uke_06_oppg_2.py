# funksjon som printer ut fra en grid, eller lister i en liste.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def render_image(grid_pattern):
    image = ''
    length_of_grid = len(grid_pattern)
    length_of_index = len(grid_pattern[0])
    for i in range(length_of_index):
        for n in range(length_of_grid):
            image += f'{grid[n][i]}'
        if i == length_of_index - 1:
            image += ''
        else:
            image += f'\n'

    return image

#print(render_image(grid))
