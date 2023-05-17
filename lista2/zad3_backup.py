import zipfile
import os
from datetime import datetime

def backup(files, save):

    """Funkcja:
        Funkcja tworząca kopie zapasową zip podanych plików
    Input:
        files (str) - pliki których kopię bezpieczeństwa chcemy utworzyć
        save (str) - lokalizacja zapisu kopii bezpieczeństwa"""

    now = datetime.now()                                                                                            #aktualna data i czas
    now = now.strftime("%Y-%m-%d_%H-%M-%S")                                                                         #zapisana w formie rok-miesiąc-dzień_godzina-minuta-sekunda

    BackupFilename = f'{now}_{os.path.splitext(os.path.basename(files))[0]}_backup.zip'                             #nazwa pliku zip (metoda tworzenia taka jak w zadaniu pdf)

    backupZip = zipfile.ZipFile(os.path.join(save, BackupFilename), 'w')                                            #otwieramy plik zip w trybie zapisu

    for katalogi, podkatalogi, pliki in os.walk(files):                                                             #po kolei w każdym katalogu i podkatalogu
        for plik in pliki:

            backupZip.write(os.path.join(katalogi, plik), os.path.relpath(os.path.join(katalogi, plik), files))     #dodajemy do kopii zapasowej

    backupZip.close()                                                                                               #zamykamy archiwum


#backup("c:/Users/User/OneDrive/Desktop/programowanie", "c:/Users/User/OneDrive/Desktop")