# Annahme: Die Eingabedatei heißt 'AdventOfCode5_1.txt'
try:
    with open('AdventOfCode5_2', 'r') as fileinput:
        lines = [line.strip() for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode5_2' wurde nicht gefunden.")
    lines = []

ranges = []
for line in lines:
    parts = line.split('-')
    if len(parts) == 2:
        ranges.append([int(parts[0]), int(parts[1])])

#Sortiert die Bereiche nach dem beginnwert
ranges.sort(key=lambda x: x[0])

merged_ranges = [ranges[0]]
for i in ranges[1:]:
    last_merged_start = merged_ranges[-1][0]
    last_merged_end = merged_ranges[-1][1]
    current_start = i[0]
    current_end = i[1]

    if current_start <= last_merged_end + 1:
        if(last_merged_end > current_end):
            merged_ranges[-1][1] = last_merged_end
        else:
            merged_ranges[-1][1] = current_end
    else:
        merged_ranges.append([current_start, current_end])

ingredients = 0
for start, end in merged_ranges:
    ingredients += (end - start + 1)

print(ingredients)
