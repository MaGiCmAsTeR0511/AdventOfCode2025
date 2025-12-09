import math

try:
    with open('AdventOfCode9_1', 'r') as fileinput:
        lines = [line.rstrip('\n') for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode8_1' wurde nicht gefunden.")
    lines = []


if not lines:
    print(0)

points = []
for line in lines:
    points.append(line.split(','))


flaeche = []
for point1 in points:
    for point2 in points:
        if point1 != point2:
            x = abs(int(point1[0])-int(point2[0]))+1
            y = abs(int(point1[1])-int(point2[1]))+1
            if x != y:
                flaeche.append(x*y)

print(max(flaeche))