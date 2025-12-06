# Annahme: Die Eingabedatei heißt 'AdventOfCode6_1.txt'
from numpy.core.defchararray import ljust
from pygments.lexer import include
from scour.scour import element
try:
    with open('AdventOfCode6_2', 'r') as fileinput:
        lines = [line.rstrip('\n') for line in fileinput]
except FileNotFoundError:
    print("Fehler: Die Eingabedatei 'AdventOfCode6_1.txt' wurde nicht gefunden.")
    lines = []

if not lines:
    print(0)
else:
    # --- TEIL 1: Probleme in Blöcke aufteilen ---

    # Schritt 1.1: Alle Zeilen auf die gleiche Länge bringen (padding)
    max_len = max(len(line) for line in lines) if lines else 0
    padded_lines = [line.ljust(max_len) for line in lines]

    # Schritt 1.2: Finde die Indizes aller leeren Spalten (Trennspalten)
    separator_indices = []
    for col_idx in range(max_len):
        if all(line[col_idx] == ' ' for line in padded_lines):
            separator_indices.append(col_idx)

    # Schritt 1.3: Benutze die Trenner, um die Blöcke auszuschneiden
    # probleme_als_bloecke wird eine Liste von Listen von Zeilen, z.B. [ [block1_zeile1, ...], [block2_zeile1, ...], ... ]
    bloecke = []
    start_col = 0
    separator_indices.append(max_len)  # Letzten Block sicher erfassen

    for end_col in separator_indices:
        if start_col < end_col:
            aktueller_block = []
            for line in padded_lines:
                block_zeile = line[start_col:end_col]
                aktueller_block.append(block_zeile)
            bloecke.append(aktueller_block)
        start_col = end_col + 1

    sum = 0
    for block in bloecke:
        mathoperator = block[-1].strip()
        lenmax = max(len(element) for element in block)
        number_list = ['' for _ in range(lenmax)]
        subresult = 0
        for element in block[:-1]:
            for stringindex in range(len(element)):
                number_list[stringindex]  += element[::-1][stringindex]
        for operand in number_list:
            if mathoperator == '+':
                subresult += int(operand)
            elif mathoperator == '*':
                if (subresult == 0):
                    subresult = int(operand)
                else:
                    subresult = int(operand) * subresult
        #print(subresult)
        sum += int(subresult)
    print(sum)

