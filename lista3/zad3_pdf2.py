import os
import PyPDF2

def pdf(folder, save, name = "polaczonyPlik.pdf"):

    """Funkcja:
        funkcja łącząca wszystkie pliki pdf w podanym folderze w jeden plik i zapisująca go w podanym mimejscu
    Input:
        folder (str) - folder w którym znajdują się pliki pdf do połączenia (zapis używając /)
        save (str) - folder zapisu (zapis używając /)
        name (str) - oczekiwana nazwa pliku z rozszerzeniem (domyślnie "polaczonyPlik.pdf)"""

    pdfPaths = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith('.pdf')]         #przeszukuje wszystkie pliki w folderze i dodaje do listy te o rozszerzeniu pdf

    pdfMerger = PyPDF2.PdfMerger()

    for pdfPath in pdfPaths:
        with open(pdfPath, 'rb') as pdfFile:                                                                #otwiera każdy plik po kolei i dodaje do tworzonego
            pdfMerger.append(pdfFile)

    outputPath = os.path.join(save, name)                                                    #tworzymy ścieżke zapisu i zapisujemy
    with open(outputPath, 'wb') as outputFile:
        pdfMerger.write(outputFile)

pdf("c:/Users/User/OneDrive/Desktop/test/pdf", "c:/Users/User/OneDrive/Desktop/test", "artykul1.pdf")

def compare(old, new):

    """Funkcja:
        Funkcja porównuje dwa pliki pdf i sprawdza czy są takie same
    Input:
        old (str) - ścieżka do pierwszego pliku pdf (zapis używając /)
        new (str) - ścieżka do drugiego pliku pdf (zapis używając /)"""

    oldPdf = PyPDF2.PdfReader(open(old, 'rb'))
    newPdf = PyPDF2.PdfReader(open(new, 'rb'))

    if len(oldPdf.pages) != len(newPdf.pages):                                              #sprawdzamy czy ilość stron sie zgadza
            return False
    
    for i in range(len(oldPdf.pages)):                                                      #porównujemy każdą strone po kolei
            oldPage = oldPdf.pages[i]
            newPage = newPdf.pages[i]

            if oldPage.extract_text() != newPage.extract_text():
                return False
    
    return True

print(compare("c:/Users/User/OneDrive/Desktop/test/artykul.pdf", "c:/Users/User/OneDrive/Desktop/test/artykul1.pdf"))