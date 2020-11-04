import math

import asciichartpy


class LossChart():
    def __init__(self, chart_height=20)


width = 90
series1 = [10 * round(math.cos(i * ((math.pi * 4) / width)), 2) for i in range(width)]
series2 = [10 * round(math.cos(i * (((math.pi-1.5) * 4) / width)), 2) for i in range(width)]

color = [asciichartpy.lightred, asciichartpy.lightblue]

print(asciichartpy.plot([series1, series2], {'height':5, 'colors':color, 'format':'{:10.1e}'}))
