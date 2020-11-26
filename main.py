import fileinput
from validators import validate_color


colors = []
for line in fileinput.input():
    line = line.lstrip()
    if validate_color(line):
        colors.append(line)
    # TODO what if else????


red_colors_sum = 0
green_colors_sum = 0
blue_colors_sum = 0

for color in colors:
    red_colors_sum += int(color[0:2], 16)
    green_colors_sum += int(color[2:4], 16)
    blue_colors_sum += int(color[4:6], 16)


red_colors_average = red_colors_sum / len(colors)
green_colors_average = green_colors_sum / len(colors)
blue_colors_average = blue_colors_sum / len(colors)

# TODO FIX TypeError when float
average_hex = hex(red_colors_average) + hex(green_colors_average) + hex(blue_colors_average)

print(average_hex)