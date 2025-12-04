try:
    with open('AdventOfCode4_2', 'r') as fileinput:
        lines = [line.strip() for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode4_1.txt' wurde nicht gefunden.")
    lines = []

a = []
rows = len(lines)
cols = len(lines[0])

a.append(['.'] * (cols + 2))
for line in lines:
    a.append(list('.' + line + '.'))
a.append(['.'] * (cols + 2))

rolls = 0

def getRoles(field, rows, cols, rolls ):
    for y in range(1, rows + 1):
        for x in range(1, cols + 1):
            if a[y][x] == '@':
                counter = 0
                if field[y - 1][x - 1] == '@': counter += 1
                if field[y - 1][x] == '@': counter += 1
                if field[y - 1][x + 1] == '@': counter += 1
                if field[y][x - 1] == '@': counter += 1
                if field[y][x + 1] == '@': counter += 1
                if field[y + 1][x - 1] == '@': counter += 1
                if field[y + 1][x] == '@': counter += 1
                if field[y + 1][x + 1] == '@': counter += 1
                if counter < 4:
                    rolls += 1
                    field[y][x] = '.'
    return field,rolls
for i in range(8000):
    field, rolls = getRoles(a, rows, cols, rolls)

print(rolls)
