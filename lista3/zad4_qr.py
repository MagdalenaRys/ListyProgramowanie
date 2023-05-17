from qrcode import QRCode
import cv2
import os

def generateQR(text, save, name = "qr.png"):

    """Funkcja:
        funkcja generująca kod qr kodujący określone dane
    Input:
        text (str) - dane do zakodowania
        save (str) - folder zapisu (zapis używając /)
        name (str) - oczekiwana nazwa pliku z rozszerzeniem (domyślnie "qr.png")"""

    qr = QRCode(version=1, box_size=15, border=1)                       #rozmiary kodu qr i jego ramki
    qr.add_data(text)                                                   #dodajemy  dane

    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")         #kolorki

    savePath =  os.path.join(save, name)                                #ścieżka zapisu
    img.save(savePath)

generateQR("www.sp30.edu.pl", "c:/Users/User/OneDrive/Desktop/test")

def readQR(file):

    """Funkcja:
        funkcja odczytująca dane z podanego kodu qr
    Input:
        file (str) - ścieżka do kodu qr
    Output:
        text (str) - odczytane dane"""

    text, kod, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(file))       #odczytuje zakodowane dane (text) oraz obszar który zajmuje kod qr na obrazku (kod)

    return text
    

print(readQR("c:/Users/User/OneDrive/Desktop/test/qr.png"))