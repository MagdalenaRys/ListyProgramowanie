import string
import random

def password(n = 8, characters = string.printable):

    """Funkcja:
        Funkcja generująca ciąg przypadkowych znaków (hasło)
    Input:
        n (int) - oczekiwana ilość znaków w haśle
        characters (str) - pula znaków z których losujemy znaki do hasła (zapisana jako ciągły tekst)
    Output:
        haslo (str) - wygenerowany ciąg znaków"""
    
    password = []                                               #tworzymy początkowo pustą liste
    
    for i in range(n):                                          #losujemy przypadkowe znaki z podanego zbioru tyle razy ile chcemy mieć znaków i dodajemy do listy
        char = random.choice(characters)
        password.append(char)
    
    haslo = ''.join(password)                                   #łączymy znaki z listy by otrzymać ciągły tekst

    return haslo

literki = string.ascii_uppercase
print("hasło (wszystkie znaki): ", password())
print("hasło (same litery drukowane): ", password(10, literki))          
print("hasło (podane znaki):", password(4, "123abc"))