try:
    with open('AdventOfCode7_2', 'r') as fileinput:
        lines = [line.rstrip('\n') for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode7_2.txt' wurde nicht gefunden.")
    lines = []

if not lines:
    print(0)
else:
    rows = len(lines)
    startx = lines[0].index('S')

    timelines = {startx: 1}
    for y in range(rows):
        next_timelines = {}
        for x, count in timelines.items():
            if y < rows and 0 <= x < len(lines[y]) and lines[y][x] == '^':
                next_timelines[x - 1] = next_timelines.get(x - 1, 0) + count
                next_timelines[x + 1] = next_timelines.get(x + 1, 0) + count
            else:
                next_timelines[x] = next_timelines.get(x, 0) + count
        print(next_timelines)
        timelines = next_timelines

    total_timelines = sum(timelines.values())
    print(total_timelines)
