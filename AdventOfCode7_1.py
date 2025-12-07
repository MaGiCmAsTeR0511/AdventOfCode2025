# Annahme: Die Eingabedatei heißt 'AdventOfCode6_1.txt'
from numpy.core.defchararray import ljust
from pygments.lexer import include
from scour.scour import element
try:
    with open('AdventOfCode7_1', 'r') as fileinput:
        lines = [line.rstrip('\n') for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode6_1.txt' wurde nicht gefunden.")
    lines = []

if not lines:
    print(0)
else:
    splitted_strings = []
    for line in lines:
        splitted_strings.append(list(line))

    sum = 0
    y = 0
    for spt in splitted_strings:
        x = 0
        for char in spt:
            if char == 'S':
                wurzel_saved_key = char
            if y > 0:
                if char == '.' and splitted_strings[y-1][x] == wurzel_saved_key :
                    splitted_strings[y][x] = '|'
                if char == '^' and splitted_strings[y-1][x] == '|' :
                    splitted_strings[y][x-1] = '|'
                    splitted_strings[y][x+1] = '|'
                    sum +=1
                if char == '.' and splitted_strings[y-1][x] == '|' :
                    splitted_strings[y][x] = '|'
            x += 1
        y += 1

    for line in splitted_strings:
        print(line)
    print(sum)