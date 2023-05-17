import argparse
from zad1_seir import seir

parser = argparse.ArgumentParser(description="Model SEIR")
parser.add_argument("-N", type=int, default=1000, help="wielkość populacji")
parser.add_argument("-S0", type=int, default=999, help="początkowa liczba zdrowych")
parser.add_argument("-E0", type=int, default=1, help="początkowa liczba chorych niezarażających")
parser.add_argument("-I0", type=int, default=0, help="początkowa liczba chorych zarażających")
parser.add_argument("-R0", type=int, default=0, help="początkowa liczba ozdrowieńców")
parser.add_argument("-beta", type=float, default=1.34, help="współczynnik zaraźliwości")
parser.add_argument("-delta", type=float, default=0.19, help="współczynnik inkubacji")
parser.add_argument("-gamma", type=float, default=0.34, help="współczynnik wyzdrowień")

dane = parser.parse_args()

N = dane.N

if dane.S0 != 999:
    roznica = dane.S0 - 999
    N += roznica

if dane.E0 != 1:
    roznica = dane.E0 - 1
    N += roznica

if dane.I0 != 0:
    roznica = dane.I0
    N += roznica

if dane.R0 != 0:
    roznica = dane.R0
    N += roznica

if N != dane.S0 + dane.E0 + dane.I0 + dane.R0:
    raise ValueError("Wielkość populacji powinna być równa sumie zdrowych, zakażonych i ozdrowieńców")
print(N)
seir(N, dane.S0, dane.E0, dane.I0, dane.R0, dane.beta, dane.delta, dane.gamma)