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


# TODO FIX zero divizion error when no colors provided
red_colors_average = red_colors_sum / len(colors)
green_colors_average = green_colors_sum / len(colors)
blue_colors_average = blue_colors_sum / len(colors)

# TODO output 00 instead of 0
average_hex = hex(round(red_colors_average)).replace('0x', '')\
              + hex(round(green_colors_average)).replace('0x', '')\
              + hex(round(blue_colors_average)).replace('0x', '')

print(average_hex)