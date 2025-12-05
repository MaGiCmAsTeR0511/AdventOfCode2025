try:
    with open('AdventOfCode5_1', 'r') as fileinput:
        lines = [line.strip() for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode4_1.txt' wurde nicht gefunden.")
    lines = []

print(lines)
ranges = []
numbers = []
ingredients = 0
for line in lines :
    elemts = line.split('-')
    if len(elemts) == 2 :
        ranges.append([int(elemts[0]), int(elemts[1])])
    else :
        if len(line) > 0 :
            numbers.append(int(line))

for number in numbers:
    for range in ranges:
        if number >= range[0] and number <= range[1]:
            ingredients +=1
            break

print(ingredients)