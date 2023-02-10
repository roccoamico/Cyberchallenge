#!/bin/env python3

import linecache

risposte_esatte = linecache.getline(r"../2023-pretest_pretest-2_1675786086.txt", 2)
fout = open("../pretest-output.txt", "w")

def calcola_punteggio(a, b):
    voto = 0
    for x, y in zip(a, b):
        if x == y:
            voto += 1
    voto -= 1
    print(voto, file=fout)


with open(r"../2023-pretest_pretest-2_1675786086.txt") as fp:
    for count, line in enumerate(fp):
        pass
    count += 2
for i in range(3, count):
    tentativo_utente = linecache.getline(r"../2023-pretest_pretest-2_1675786086.txt", i)
    calcola_punteggio(risposte_esatte, tentativo_utente)
