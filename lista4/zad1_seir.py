import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sys

def seir(N, S0, E0, I0, R0, beta, delta, gamma):

    """Funkcja
        Funkcja tworząca wykres przebiegu pandemii w zależności od podanych parametrów
    Input:
        N (int) - wielkość populacji
        S0 (int) - początkowa liczba osób zdrowych
        E0 (int) - początkowa liczba osób chorych niezarażających
        I0 (int) - początkowa liczba osób chorych zarażających
        R0 (int) - początkowa liczba ozdrowieńców
        beta (float) - współczynnik zaraźliwości
        delta (float) - współczynnik inkubacji
        gamma (float) - współczynnik wyzdrowień"""

    def rownanka(y, t, N, beta, gamma, delta):                          #równanka z modelu SEIR

        S, E, I, R = y 
        dsdt = -beta*S*I/N
        dEdt = beta*S*I/N - delta*E
        dIdt = delta*E - gamma*I
        dRdt = gamma*I

        return dsdt, dEdt, dIdt, dRdt

    t = np.linspace(0, 100, 100)                                        #jak długo ma ta symulacja trwać, tu dałam 100 dni 
    y0 = S0,  E0, I0, R0 

    wyniki = odeint(rownanka, y0, t, args=(N, beta, gamma, delta))      #podajemy tu funkcję (rownanka), wartości początkowe (y0), podział czasu (t) i inne potrzebne do wykonania funkcji wartości (args) 
    S, E, I, R = wyniki.T                                               #T transponuje tą macierz żeby nam pasowała do obliczeń

    plt.plot(t, S, label="Zdrowi")
    plt.plot(t, E, label="Zarażeni niezakażający")
    plt.plot(t, I, label="Zarażeni zakażający")
    plt.plot(t, R, label="Ozdrowieńcy")
    plt.legend()
    plt.axhline(y=0, color="Lightgrey")
    plt.xlabel("Czas (dni)")
    plt.ylabel("Liczba osób")
    plt.title("Model SEIR")
    plt.savefig("seir.png")
    plt.show()

if __name__ == "__main__":
    N, S0, E0, I0, R0, beta, delta, gamma = [float(x) for x in sys.argv[1:]]
    if N != S0 + E0 + I0 + R0:
        raise ValueError("Wielkość populacji powinna być równa sumie zdrowych, zakażonych i ozdrowieńców")
    seir(N, S0, E0, I0, R0, beta, delta, gamma)
