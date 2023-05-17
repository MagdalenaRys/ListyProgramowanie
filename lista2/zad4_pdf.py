import os
import PyPDF2

def split(file, n, save):

    """Funkcja:
        Funkcja rozddielająca plik pdf na kilka mniejszych
    Input:
        file (str) - nazwa/lokalizacja pliku pdf (używając "/")
        n (int) - liczba stron w tworzonych krótszych plikach
        save (str) - folder zapisu utworzonych plików pdf (używając "/")"""

    pdfFile = open(file, "rb")
    pdfRead = PyPDF2.PdfReader(pdfFile)

    AllPages = len(pdfRead.pages)                                                                   #ile stron ma plik
    AllParts = AllPages // n + (1 if AllPages % n != 0 else 0)                                      #na ile części dzielimy plik

    for i in range(AllParts):                                                                       #powtarzamy pętle tyle razy ile jest części

        start = i*n                                                                                 #jaka jest strona poczatkowa i końcowa danej części
        end = min(start + n, AllPages)                                                              #zapobiega to błędowi spowodowanemu liczbą stron niepodzielną przez n

        pdfWrite = PyPDF2.PdfWriter()

        for j in range(start, end):                                                                 #dodajemy strony od początkowej do końcowej
            pdfWrite.add_page(pdfRead.pages[j])

        FileName = os.path.splitext(os.path.basename(file))[0] + f"_part{i+1}_pages{start+1}-{end}.pdf"       #tworzymy plik z daną częścią
        partPath = os.path.join(save, FileName)                                                     #nazwa powstaje poprzez rozdzielenie nazwy pliku (tworzy liste ["artykul", "pdf"], wybraniu nazwy bez rozszerzenia i dopisaniu numerów stron)
        partFile = open(partPath, "wb")                                                             #następnie zapisujemy ją w lokalizacji wybrany katalog zapisu + utworzona nazwa
        pdfWrite.write(partFile)                                                                    #otwiera utworzoną lokalizacje (read mode), nadpisuje utworzony plik i zamyka
        partFile.close()

    pdfFile.close()
    

split("C:/Users/User/OneDrive/Desktop/test/artykul.pdf", 3, "C:/Users/User/OneDrive/Desktop/test/pdf")