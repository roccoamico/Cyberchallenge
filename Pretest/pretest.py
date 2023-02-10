#!/bin/env python3

import linecache

risposte_esatte = linecache.getline(r"2023-pretest_pretest-1_1675783900.txt", 2)
tentativo_utente = linecache.getline(r"2023-pretest_pretest-1_1675783900.txt", 3)
fout = open("../pretest-output.txt", "w")


def calcola_punteggio(a, b):
    voto = 0
    for x, y in zip(a, b):
      if x == y:
        voto += 1
    voto -= 1
    print(voto, file=fout)


calcola_punteggio(risposte_esatte, tentativo_utente)
