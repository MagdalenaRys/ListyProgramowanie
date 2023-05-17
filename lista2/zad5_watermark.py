from PIL import Image

def watermark(file, watermarkFile, transparency, save):

    """Funkcja:
        Funkcja dodająca znak wodny do podanego obrazu
    Input:
        file (str) - nazwa/lokalizacja obrazu (używając "/")
        watermarkFile (str) - nazwa/lokalizacja obrazu, który ma zostać znakiem wodnym (używając "/")
        transparency (float) - intensywność znaku wodnego (w skali 0-1, gdzie 1 to całkowicie widoczny, a 0 to całkowicie przezroczysty)
        save (str) - oczekiwana nazwa/lokalizacja obrazu z nałożonym znakiem wodnym (używając "/")"""

    originalImage = Image.open(file)                                            #otwieramy oba zdjęcia, a zdjęcie które ma być znakiem wodnym w trybie RGBA
    watermark = Image.open(watermarkFile).convert('RGBA')

    alpha = int(transparency*255)                                               #na podstawie oczekiwanej intensywności obliczamy alphe
    watermark.putalpha(alpha)

    width, height = originalImage.size                                          #wkleja utworzony znak wodny w prawy dolny róg oryginalnego obrazu
    x = (width - watermark.width)//2
    y = (height - watermark.height)//2
    originalImage.paste(watermark, (x, y), watermark)

    originalImage.save(save)


#watermark("C:/Users/User/OneDrive/Desktop/test/zdjecie.jpeg", "C:/Users/User/OneDrive/Desktop/test/kot.jpeg", 0.4, "C:/Users/User/OneDrive/Desktop/test/efekty.jpg")