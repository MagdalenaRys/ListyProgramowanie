def addition(operation):

    """Funkcja:
        Funkcja zwracająca słupek odpowiadający podanemu dodawaniu  liczb naturalnych
    Input:
        operation (str) - podane w formie tekstu dodawanie (używając jedynie liczb całkowitych i znaku +, bez spacji i nawiasów (dla liczb ujemnych zapisujemy liczba+-liczba))
        przykład: "37+22+-24"
    Output:
        output (str) - odpowiadający podanemu działaniu słupek"""

    numbers = operation.split("+")                                  #rozdzielamy liczby oddzielone znakiem dodawania
    intNumbers = [int(x) for x in numbers]                          #zamieniamy elementy listy z str na int
    result = sum(intNumbers)                                        #wynik działania

    maximum = max(intNumbers)                                       #szukamy najdłuższej liczby (będzie to jednocześnie ta największa)
    length = len(str(maximum)) + 2                                  #szerokość słupka (o dwa większa od długości najdłuższej liczby)

    output = ""
    for n in range(len(intNumbers)-1):                              #po kolei dopisujemy każdą liczbe do naszego słupka (poza ostatnią)
        output += f"{intNumbers[n]:>{length}}\n"                    #zapis :>{liczba} pozwala na zformatowanie tekstu tak, by zajął odpowiedną długość linijki
    
    output += f"+{intNumbers[len(intNumbers)-1]:>{length-1}}\n"     #przed ostatnią liczbą dopisujemy znak dodawania
    output += f"{'-' * length}\n"                                   #kreska
    output += f"{result:>{length}}\n"                               #wynik

    return output

def subtraction(operation):                                         #prawie wszystko analogicznie

    """Funkcja:
        Funkcja zwracająca słupek odpowiadający podanemu odejmowaniu  liczb naturalnych
    Input:
        operation (str) - podane w formie testu odejmowanie (używając jedynie liczb naturalnych i znaku -, bez spacji i nawiasów i nawiasów (dla liczb ujemnych zapisujemy liczba--liczba))
    Output:
        output (str) - odpowiadający podanemu działaniu słupek"""

    numbers = operation.split("-")
    intNumbers = [int(x) for x in numbers]
    
    result = intNumbers[0]
    for i in range(len(intNumbers)-1):                              #tu wynik otrzymujemy poprzez odejmowanie w pętli wszystkich liczb od tej pierwszej
        result -= intNumbers[i+1]

    maximum = max(intNumbers)
    length = len(str(maximum)) + 2
    
    output = ""
    for n in range(len(intNumbers)-1):
        output += f"{intNumbers[n]:>{length}}\n"
    
    output += f"-{intNumbers[len(intNumbers)-1]:>{length-1}}\n"
    output += f"{'-' * length}\n"
    output += f"{result:>{length}}\n"

    return output

def multiplication(operation):

    """Funkcja:
        Funkcja zwracająca słupek odpowiadający podanemu mnożeniu liczb naturalnych
    Input:
        operation (str) - podane w formie testu mnożenie (używając jedynie liczb naturalnych i znaku *, bez spacji i nawiasów (dla liczb ujemnych zapisujemy liczba*-liczba)
    Output:
        output (str) - odpowiadający podanemu działaniu słupek"""

    numbers = operation.split("*")
    intNumbers = [int(x) for x in numbers]
    
    result = intNumbers[0]
    for i in range(len(intNumbers)-1):
        result *= intNumbers[i+1]

    maximum = max(intNumbers)
    length = len(str(maximum)) + 2
    
    output = ""
    for n in range(len(intNumbers)-1):
        output += f"{intNumbers[n]:>{length}}\n"
    
    output += f"*{intNumbers[len(intNumbers)-1]:>{length-1}}\n"
    output += f"{'-' * length}\n"
    output += f"{result:>{length}}\n"

    return output

print(addition("-4555+7253+-345"))
print(subtraction("500-2255-23"))
print(addition("500+-2255+-23"))
print(multiplication("22*-3*125"))