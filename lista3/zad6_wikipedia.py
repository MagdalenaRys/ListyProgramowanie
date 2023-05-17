import requests
from bs4 import BeautifulSoup
import webbrowser

def getArticle():

    """Funkcja:
        funkcja losująca przypadkowy artykuł z wikipedii i zwracająca jej tytuł i adres
    Output:
        title (str) - tytuł wylosowanego artykułu
        page (str) - adres wylosowanego artykułu"""

    page = requests.get(f"https://en.wikipedia.org/wiki/Special:Random")                    #request pobiera strone HTML z adresu URL                            
    soup = BeautifulSoup(page.content, "html.parser")                                       #BeautifulSoup odczytuje zawartość strony
    title  = soup.find(class_="firstHeading").text                                          #i znajduje tytuł artykułu

    return title, page.url

for i in range(100):

    title, page = getArticle()
    anwser = input(f"Wylosowany artykuł to: {title} \n Czy chcesz otworzyć artykuł w przeglądarce? (T/N)").upper()

    if anwser == "T":
        webbrowser.open(page)
        break
    elif anwser == "N":
        print("kolejna próba:")
    else:
        print("Podaj odpowiedź w formie T/N")
