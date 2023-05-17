from PIL import Image

def miniatura(file, size, save):

    """Funkcja:
        Funkcja generująca miniaturę obrazu
    Input:
        file (str) - nazwa/lokalizacja obrazu (używając "/")
        size (list) - rozmiar miniatury
        save (str) - nazwa/lokalizacja miniatury (używając "/")"""

    img = Image.open(file)
    img.thumbnail(size)
    img.save(save)

#miniatura("C:/Users/User/OneDrive/Desktop/test/zdjecie.jpeg", [100, 100], "c:/Users/User/OneDrive/Desktop/test/miniatura.jpg")