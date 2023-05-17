def zamianka(path):

    """Funkcja:
        Funkcja zamienia znaki końca linii z windowsowych na linuksowe
    Input:
        path (str) - ścieżka do pliku w którym chcemy te znaki zamienić"""

    file = open(path, "rb+")
    text = file.read()

    if b"\r\n" in text:                             #zamieniamy windowsowe "\r\n" (CRLT) na linuksowe "\n" (LF)
        text = text.replace(b"\r\n", b"\n")
    else:
        text = text.replace(b"\n", b"\r\n")         #zamieniamy linuksowe "\n" na windowsowe "\r\n"

    file.seek(0)                                    #przerzuca kursor na początek pliku??
    file.write(text)                                #nadpisuje zmiany
    file.truncate()                                 #usuwa wszystko co znajduje sie po aktulnej pozycji wskaźnika w pliku

zamianka("c:/Users/User/OneDrive/Desktop/test/tekst.txt")

#sprawdzić sie to da w bashu komendą "od -c tekst.txt"