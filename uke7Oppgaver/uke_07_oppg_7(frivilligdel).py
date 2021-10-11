# plot funksjon som tar koordinater av form (x, y) og gir ut et plot

def render_plot(coordinates):
    plot = ''

    # multiple assignment
    x_coordinates, y_coordinates = zip(*coordinates)

    max_x = max(x_coordinates)
    min_x = min(x_coordinates)
    max_y = max(y_coordinates)
    min_y = min(y_coordinates)

    width = len(range(min_x, max_x))

    # Topp og bunn av plottet
    top_and_bottom = '#' * (width + 3)

    plot_points = ''
    for y in range(max_y, min_y - 1, -1):
        plot_points += '#'
        for x in range(min_x, max_x + 1):
            if (x, y) in coordinates:
                plot_points += '*'
            elif x == min_x + 1:
                plot_points += '|'
            elif y == min_y + 1:
                plot_points += '-'
            else:
                plot_points += ' '
        plot_points += '#\n'

    plot = top_and_bottom + '\n' + plot_points + top_and_bottom

    return plot

# test
print(render_plot([(2, 3), (-1, 2), (1, -1), (0, 1), (4, 4)]))