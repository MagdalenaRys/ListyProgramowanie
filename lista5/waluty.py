import tkinter as tk
from tkinter import ttk
import requests
import json
from datetime import datetime
    
def LoadData():

    """Funkcja:
        funkcja pobierająca aktualne przeliczniki walut ze strony NBP (lub używająca najbardziej aktualnej uprzednio pobranej w wypadku braku połączenia z internetem)
    Output:
        currency (dict) - słownik zawierający nazwy walut i ich przeliczniki (w złotówkach)
        time (str) - data pochodzenia danych 
        online (bool) - informacja, czy dane są aktualne"""
    
    online = True

    try:
        page = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
        currencyData = json.loads(page.text)[0]['rates']

        time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        data = {'time': time, 'currencyData': currencyData}

        with open("currencyData.json", "w") as file:
            json.dump(data, file)

    except requests.exceptions.RequestException:
        with open("currencyData.json", "r") as file:
            data = json.load(file)
            time = data['time']
            currencyData = data['currencyData']
            online = False
    
    currency = {'złoty': 1.0}
    for el in currencyData:
        name = el['currency']
        value = el['mid']
        currency[name] = value

    return currency, time, online

def create():
    """Funkcja:
        funkcja tworząca interfejs graficzny kalkulatora walut"""

    dane, time, online = LoadData()
    waluty = [*dane]

    root = tk.Tk()
    root.title("Kalkulator walut")
    root.geometry('449x500')
    root.resizable(height=False, width=False)

    titleFrame = tk.Frame(root, bg="#2C5F2D")
    titleFrame.grid(row=0, column=0)

    nameLabel = tk.Label(titleFrame, text='Kalkulator Walut', bg="#2C5F2D", fg="white", pady=30, padx=24, justify="center", font=('Helvatica 38 bold'))
    nameLabel.grid(row=0, column=0)

    mainFrame = tk.Frame(root, bg='#97BC62', width=450, height=250)
    mainFrame.grid(row=1, column=0)

    firstCurrencyLabel = tk.Label(mainFrame, text="Waluta źródłowa:", bg= '#97BC62', font=('Helvatica 10 bold'))
    firstCurrencyLabel.place(x=5, y=10)

    firstCurrencyVar = tk.StringVar()
    firstCurrencyOptions = ttk.Combobox(mainFrame, font=('Helvatica 10'), width=20, textvariable=firstCurrencyVar, values=waluty)
    firstCurrencyOptions.place(x=5, y=35)

    cashLabel = tk.Label(mainFrame, text="Kwota:", bg= '#97BC62', font=("Helvatica 10 bold"))
    cashLabel.place(x=255, y=10)

    amount = tk.Entry(mainFrame, width=20)
    amount.place(x=255, y=35)

    secondCurrencyLabel = tk.Label(mainFrame, text="Waluta docelowa:", bg= '#97BC62', font=("Helvatica 10 bold"))
    secondCurrencyLabel.place(x=5, y=80)

    secondCurrencyVar = tk.StringVar()
    secondCurrencyOptions = ttk.Combobox(mainFrame, font=('Helvatica 10'), width=20, textvariable=secondCurrencyVar, values=waluty)
    secondCurrencyOptions.place(x=5, y=105)

    resultLabel = tk.Label(mainFrame, text="Wynik:", bg= '#97BC62', font=("Helvatica 10 bold"))
    resultLabel.place(x=255, y=80)

    resultVar = tk.StringVar()
    result = tk.Entry(mainFrame, font=('Helvatica 10'), width=17, state="readonly", textvariable=resultVar)
    result.place(x=255, y=105)

    bottomFrame = tk.Frame(root, bg="#2C5F2D", width=450, height=130)
    bottomFrame.grid(row=2, column=0)

    bottomLabel = tk.Label(bottomFrame, text="Uwagi:", bg="#2C5F2D", fg="white", font=('Helvatica 20 bold'))
    bottomLabel.place(x=5, y=10)

    infoLabel = tk.Label(bottomFrame, text="Należy podać kwotę używając jedynie cyfr i kropki", bg="#2C5F2D", fg="white", font=('Helvatica 10 bold'))
    infoLabel.place(x=5, y=48)

    onlineInfoLabel = tk.Label(bottomFrame, text="", bg="#2C5F2D", fg="white", font=('Helvatica 10 bold'))
    onlineInfoLabel.place(x=5, y=70)

    if not online:
        onlineInfoLabel.config(text= f"Brak połączenia z internetem, dane pochodzą z {time}")
    else:
        onlineInfoLabel.config(text= f"Dane są aktualne :)        ({time})")

    errorLabel = tk.Label(bottomFrame, text="", bg="#2C5F2D", fg="white", font=('Helvatica 10 bold'))
    errorLabel.place(x=5, y=95)

    def count():
        
        """Funkcja:
            funkcja obliczająca przelicznik wybranych dwóch walut"""
        
        firstCur = firstCurrencyVar.get()
        secondCur = secondCurrencyVar.get()
        value = amount.get()

        if not value:
            errorLabel.config(text="Wprowadź kwotę!")
            return
        try:
            value = float(value)
        except ValueError:
            errorLabel.config(text="Nieprawidłowa kwota!")
            return
        
        firstValue = float(dane[firstCur])
        secondValue = float(dane[secondCur])

        result = value * (firstValue / secondValue)
        resultVar.set(str(result))
        errorLabel.config(text="")

    calculateButton = tk.Button(mainFrame, text="Oblicz", command=count, bg= "#2C5F2D", fg="white", font=('Helvatica 10 bold'))
    calculateButton.place(x=200, y=150)

    quitButton = tk.Button(mainFrame, text="Zakończ", command=root.destroy, bg= "#2C5F2D", fg="white", font=('Helvatica 10 bold'))
    quitButton.place(x=193, y=190)

    root.mainloop()

create()