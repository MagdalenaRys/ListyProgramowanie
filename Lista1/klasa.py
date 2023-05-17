import numpy as np
import math

class Vector:

    def __init__(self, arg = 3):

        """Funkcja:
            konstruktor klasy Vector
        Input:
            arg (int) - oczekiwana ilość elementów w wektorze (domyślnie 3)"""

        self.arg = arg
        self.v = []
        for i in range(self.arg):
            self.v.append(0)

    def RandomElements(self):

        """Funkcja:
            funkcja zamieniająca elementy wektora na przypadkowe liczby rzeczywiste
        Output:
            v (list) - wektor po zmianie"""

        for i in range(self.arg):
            k = np.random.randn()                                                                             #to są przypadkowe czy niebardzo????
            self.v[i] = k
        return self.v

    def GivenElements(self, elements):

        """Funkcja:
            funkcja zamieniająca elementy wektora na podane
        Input:
            elements (list) - lista z oczekiwanymi elementami
        Output:
            v (list) - wektor po zmianie"""

        if len(self.v) != len(elements):
            raise ValueError("podana lista musi być tej samej długości co wektor")
        else:

            for i in range(len(self.v)):
                self.v[i] = elements[i]
            return self.v
        
    def __add__(self, w):

        """Funkcja:
            funkcja dodająca dwa podane wektory
        Input:
            w (list) - drugi podany wektor
        Output:
            v (list) - wektor po wykonaniu dodawania"""

        if len(self.v) != len(w):
            raise ValueError("dodawane wektory muszą być tej samej długości")
        else:
            
            for i in range(len(self.v)):
                self.v[i] = self.v[i] + w[i]
                
            return self.v

    def __sub__(self, w):

        """Funkcja:
            funkcja odejmująca od wektora podany wektor
        Input:
            w (list) - podany wektor
        Output:
            v (list) - wektor po wykonaniu odejmowania"""

        if len(self.v) != len(w):
            raise ValueError("odejmowane wektory muszą być tej samej długości")
        else:
            for i in range(len(self.v)):
                self.v[i] = (self.v)[i] - w[i]
            return self.v

    def Multiply(self, n):

        """Funkcja:
            funkcja mnożąca wektor przez podany skalar
        Input:
            n (float) - skalar
        Output:
            v (list) - wektor po wykonaniu mnożenia"""
        
        iloczyn = []
        for i in range(len(self.v)):
            iloczyn.append(n*((self.v)[i]))
        
        self.v = iloczyn
        return self.v

    def Length(self):
    
        """Funkcja:
            funkcja obliczająca długość danego wektora
        Output:
            length (float) - długość wektora"""
        
        squares = []
        for i in self.v:
            squares.append(i**2)

        suma = sum(squares)
        length = math.sqrt(suma)
        return length

    def AddElements(self):

        """Funkcja:
            funkcja dodająca elementy składowe wektora
        Output:
            sumaElementow (float) - suma elementów składowych wektora"""
        
        sumaElementow = sum(self.v)
        return sumaElementow

    def __mul__(self, w):

        """Funkcja:
            funkcja obliczająca iloczyn skalarny dwóch wektorów
        Input:
            w (list) - drugi wektor
        Output:
            result (float) - iloczyn skalarny podanych dwóch wektorów"""
        
        if len(self.v) != len(w):
            raise ValueError("mnożone wektory muszą być tej samej długości")
        else:
            iloczyny = []
            for i in range(len(w)):
                iloczyny.append(((self.v)[i])*(w[i]))
            result = sum(iloczyny)
    
            return result

    def __str__(self):

        """Funkcja:
            Funkcja reprezentująca obiekt tekstowo
        Output:
            (str) - reprezentacja tekstowa obiektu"""

        return("wektor: " + str(self.v))

    def __getitem__(self, key):

        """Funkcja:
            funkcja zwracająca element składowy o wybranym indeksie
        Input:
            key (int) - wybrany indeks
        Output:
            self.v[key] (float) - element składowy o podanym indeksie"""
    
        return self.v[key]
       
    
    def __contains__(self, item):

        """Funkcja:
            funkcja sprawdzająca czy dany element jest elementem składowym wektora
        Input:
            item (float) - szukany element
        Output:
            True/False (bool) - zwracana wartość logiczna zdania"""

        count = (self.v).count(item)
        
        if count > 0:
            return True
        else:
            return False
        
    def __len__(self):

        """Funkcja:
            funkcja zwracająca ilość elementów danego wektora
        Output:
            self.arg (int) - ilość elementów danego wektora"""

        return self.arg