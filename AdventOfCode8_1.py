import math

try:
    with open('AdventOfCode8_1', 'r') as fileinput:
        lines = [line.rstrip('\n') for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode8_1' wurde nicht gefunden.")
    lines = []


def linedistance(startpoint, endpoint):
    distance = math.sqrt((int(endpoint[0]) - int(startpoint[0]))**2 + (int(endpoint[1]) - int(startpoint[1]))**2 + (int(endpoint[2]) - int(startpoint[2]))**2)
    return distance

if not lines:
    print(0)
else:
    points = []
    for line in lines :
        points.append(line.split(','))

    distances = []
    index1 = 0
    for point1 in points:
        index2 = 0
        for point2 in points:
            if point1[0] != point2[0] and (linedistance(point1,point2),[point2,point1]) not in distances:
                distances.append((linedistance(point1,point2),[point1,point2]))
            index2 +=1
        index1 += 1
    distances.sort()

    junction_points = []

    for distance in distances:
        junction_points.append(distance[1])


    junction_boxes = []
    junction_index = 0
    for junction_point in junction_points:
        if junction_index < 10:
            if(junction_index < len(junction_points)-1) and junction_index !=0:
                for i in range(len(junction_boxes)):
                    if junction_point[0] in junction_boxes[i]:
                        junction_boxes[i].append(junction_point[0])
                    elif junction_point[1] in junction_boxes[i]:
                        junction_boxes[i].append(junction_point[1])
                    else:
                        junction_boxes.append(junction_point)
            else:
                junction_boxes.append(junction_point)
        junction_index += 1
print(junction_boxes)