from zipfile import ZipFile
import os
from datetime import datetime

def copy(dirs, extensions, save = "c:/Users/User/OneDrive/Desktop", days = 3):

    """Funkcja:
        Funkcja tworzy kopie zapasowe plików o podanych rozszerzeniach w podanych katalogach utworzonych w ciągu ostatnich dni i zapisuje je w określonym miejscu
    Input:
        dirs (list) - ścieżki kaalogów w których będziemy szukać plików (zapis jako str używając /; np. ["c:/Users/User/OneDrive/Desktop/test", "c:/Users/User/OneDrive/Desktop/programowanie"])
        extensions (list) - wybrane rozszerzenia (zapis jako str; np. [".pdf", ".py"])
        save (str) - ścieżka zapisu (zapis używając /) (domyślnie pulpit)
        days (int) - z ilu dni wstecz zapisujemy pliki (domyślnie 3)"""

    now = datetime.now()
    nowStr = now.strftime('%Y-%m-%d')                                           #odczytujemy aktualną date

    ZipName = f"copy_{nowStr}.zip"                                              #tworzymy nazwe zipa

    backupDir = os.path.join(save, "backup")          

    if not os.path.exists(backupDir):                                           #w oczekiwaniej ścieżce zapisu tworzymy folder backup (jeśli ten nie istnieje)    
        os.makedirs(backupDir)

    backupZip = ZipFile(os.path.join(backupDir, ZipName), 'w')

    for dir in dirs:                                                            #w każdym podanym katalogu, po kolei w każdym podkatalogu i pliku (dokładnie tak jak na poprzedniej liście)
        for katalogi, podkatalogi, pliki in os.walk(dir):
            for plik in pliki:
                
                if os.path.splitext(plik)[1] in extensions:                     #sprawdzamy czy rozszerzenie jest wśród tych podanych
                    
                    filePath = os.path.join(katalogi, plik)
                    fileTime = os.path.getmtime(filePath)                       #odczytujemy ścieżke i czas ostatniej modyfikacji
                    fileAge = now - datetime.fromtimestamp(fileTime)            #sprawdzamy "wiek" pliku
                    
                    if fileAge.days <= days:                                    #jeśli ma wystarczająco mało dni to dodajemy do zipa
                        
                        backupZip.write(os.path.join(katalogi, plik), os.path.relpath(os.path.join(katalogi, plik), dir))

dirs = ["c:/Users/User/OneDrive/Desktop/test", "c:/Users/User/OneDrive/Desktop/programowanie"]
extensions = [".pdf", ".txt", ".py"]

copy(dirs, extensions, "c:/Users/User/OneDrive/Desktop")
