from klasa import Vector

print("\ntworzenie wektora:")
wektor = Vector()
wektor1 = Vector(5)
print(wektor, wektor1)

print("\nnadawanie wektorowi przypadkowych współrzędnych:")
wektor.RandomElements()
wektor1.RandomElements()
print(wektor, wektor1)

print("\nnadawanie wektorowi konkretnych współrzędnych:")
wektor.GivenElements([0, 1, 2])
wektor1.GivenElements([0, 1, 2, 3, 4])
print(wektor, wektor1)

#tworzymy wektory potrzebne do dalszych obliczeń
wektor2 = Vector()
wektor2.GivenElements([2, 2, 2])
wektor3 = Vector(5)
wektor3.GivenElements([2, 2, 2, 2, 2])

print("\nsuma dwóch wektorów:")
print(wektor + wektor2)
print(wektor1 + wektor3)

print("\nróżnica dwóch wektorów:")
print(wektor - wektor2)
print(wektor1 - wektor3)

print("\nmnożenie wektora przez skalar:")
print(wektor.Multiply(3))
print(wektor1.Multiply(2))

print("\nobliczanie długości wektora:")
print(wektor.Length())
print(wektor1.Length())

print("\nsumowanie elementów składowych wektora:")
print(wektor.AddElements())
print(wektor1.AddElements())

print("\nobliczanie iloczynu skalarnego wektorów:")
print(wektor*wektor2)
print(wektor1*wektor3)

print("\notrzymywanie określonego elementu składowego wektora:")
print(wektor[2])
print(wektor1[1])

print("\nszukanie danego elementu wśród składowych wektora:")
print(2 in wektor)
print(6 in wektor)
print(3 in wektor1)
print(5 in wektor1)

#sprawdzenie błędów
print("\nbłąd przy podaniu listy o innej długości niż wektor przy nadawaniu współrzędnych")
wektor.GivenElements([1, 2, 3, 4])

print("\nbłąd przy mnożeniu wektorów o różnych długościach (analogicznie przy dodawaniu, odejmowaniu)")
wektor*wektor1