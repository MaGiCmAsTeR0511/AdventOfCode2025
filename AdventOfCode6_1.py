try:
    with open('AdventOfCode6_1', 'r') as fileinput:
        lines = [line.strip().split(" ") for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode4_1.txt' wurde nicht gefunden.")
    lines = []
result =[]
for line in lines:
    result.append(list(filter(lambda x: x != "", line)))

#Get the Operator with reverse the List and get the first index
mathoperator = result[-1]
del result[-1]

ergebnis = 0
for operator in  range(len(mathoperator)):
    subresult = 0
    matho = mathoperator[operator]
    for operand in result :
        match matho:
            case '+':
                subresult += int(operand[operator])
            case '*':
                if(subresult ==0):
                    subresult = int(operand[operator])
                else:
                    subresult = int(operand[operator]) * subresult
    ergebnis += int(subresult)

print(ergebnis)

