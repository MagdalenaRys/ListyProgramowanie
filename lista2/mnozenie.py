def multiplication2(operation):

    """Funkcja:
        Funkcja zwracająca słupek odpowiadający podanemu mnożeniu liczb naturalnych
    Input:
        operation (str) - podane w formie testu mnożenie (używając jedynie dwóch liczb całkowitych i znaku *, bez spacji)
    Output:
        output (str) - odpowiadający podanemu działaniu słupek"""

    numbers = operation.split("*")
    intNumbers = [int(x) for x in numbers]

    if len(numbers) != 2:                                                       #mnożymy w słupku tylko dla dwóch liczb (chyba?)
        raise ValueError("podano więcej niż dwie liczby")
    
    result = intNumbers[0]                                                      #obliczamy wynik tak samo jak poprzednio
    for i in range(len(intNumbers)-1):
        result *= intNumbers[i+1]

    maximum = max(intNumbers)
    length = len(str(maximum)) + 3
    
    output = ""
    for n in range(len(intNumbers)-1):                                          #i tworzymy słupek też tak samo
        output += f"{intNumbers[n]:>{length}}\n"
    
    output += f"*{intNumbers[len(intNumbers)-1]:>{length-1}}\n"
    output += f"{'-' * length}\n"

    pierwszaLiczba = intNumbers[0]                                              #rozdzielamy te dwie liczby żeby policzyć ten środek słupka
    drugaLiczba = numbers[1]                                                    #pierwsza ma być jako int a druga jako str

    listaDruga = []                                                             #tworzymy liste składającą się z cyfr liczby drugiej (dlatego liczba druga musiała być str)
    for i in range(len(drugaLiczba)):                                           #odwracamy kolejność listy (bo w mnożeniu w słupku mnożymy "od tyłu")
        listaDruga.append(drugaLiczba[i])                                       #i zamieniamy elementy listy na int żeby dało sie mnożenie wykonać
    listaDruga.reverse()
    listaDruga = [int(x) for x in listaDruga]

    for i in range(len(listaDruga)):                                            #przemnażamy liczbe pierwszą przez każdą cyfre liczby drugiej
        lista = []                                                              #i dodajemy jako linijke w słupku tą samą metodą co wcześniej
        lista.append(listaDruga[i]*pierwszaLiczba)
        lista = [str(x) for x in lista]
        linijka = ''.join(lista)
        output += f"{linijka:>{length}}"+" "*(i)+"\n"


    output += f"{'-' * length}\n"
    output += f"{result:>{length}}\n"

    return output

print(multiplication2("422*54"))
print(multiplication2("5634*28"))