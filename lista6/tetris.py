import pygame
from pygame import mixer
from copy import deepcopy
from random import choice
import json
import os

width, height = 8, 15
tile = 45
gameField = width * tile, height * tile
screenField = 720, 710
fps = 60

pygame.init()                                                               #otwieramy pygame i tworzymy okienko i pole z podziałką
mixer.init()
screen = pygame.display.set_mode(screenField)
pygame.display.set_caption("Tetris :)")
gameScreen = pygame.Surface(gameField)
clock = pygame.time.Clock()
grid = [pygame.Rect(x * tile, y * tile, tile, tile) for x in range(width) for y in range(height)]

pygame.mixer.music.load("images/theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
pygame.mixer.music.get_busy()

figuresPositions = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],                     #możliwe ułożenia poczwórnych bloczków w układzie współrzędnych
                    [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                    [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figures = [[pygame.Rect(x + width // 2, y + 1, 1, 1) for x, y in position] for position in figuresPositions]  #i ich wywołanie w pygame
figureRect = pygame.Rect(0, 0, tile - 2, tile - 2)
field = [[0 for _ in range(width)] for _ in range(height)]

animCount, animSpeed, animLimit = 0, 60, 2000

background = pygame.image.load("images/background.jpg").convert()               #tła, czcionki, teksty itd
gameBackground = pygame.image.load("images/background2.jpg").convert()

mainFont = pygame.font.Font("images/font.ttf", 65)
font = pygame.font.Font("images/font.ttf", 45)
miniFont = pygame.font.Font("images/font.ttf", 25)

class Menu:                                                                     #budujemy menu
    def __init__(self):
        """Funkcja:
            konstruktor klasy menu"""
        self.buttons = []

    def addButton(self, button):
        """Funkcja:
            funkcja dodająca do listy buttons określony przycisk
        Input:
            button (class object) - dodawany do menu przycisk """
        self.buttons.append(button)

    def draw(self, screen):
        """Funkcja:
            funkcja rysująca przyciski na ekranie
        Input:
            screen - okienko w pygame czy coś"""
        for button in self.buttons:
            button.draw(screen)

    def click(self, pos):
        """Funkcja:
            funkcja powodująca reakcję na kliknięcie przycisku
        Input:
            pos (tuple ?) - miejsce kliknięcia"""
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                button.clikk()

class Button:                                                                   #i guziki też
    def __init__(self, label, position, action):
        """Funkcja:
            konstruktor klasy button
        Input:
            label (str) - nazwa przycisku
            position (tuple) - pozycja przycisku
            action (function) - co ma robić ten przycisk"""
        self.label = label
        self.position = position
        self.action = action
        self.rect = pygame.Rect(position[0], position[1], 250, 70)

    def draw(self, screen):
        """Funkcja:
            funkcja rysująca przycisk
        Input:
            screen - okienko w pygame chyba"""
        pygame.draw.rect(screen, ("#FFF5B8"), self.rect)
        text = font.render(self.label, True, (0, 0, 0))
        textRect = text.get_rect(center=self.rect.center)
        screen.blit(text, textRect)

    def clikk(self):
        """Funkcja:
            funkcja sprawiająca że guzik wykonuje akcje"""
        self.action()


def startGame():                                                                #definiujemy co te guziki mają robić
    """Funkcja:
        funkcja definująca stan jako stan gry"""
    global gameState
    gameState = "game"

def showRules():
    """Funkcja:
        funkcja definująca stan jako stan zasad"""
    global gameState
    gameState = "rules"

def showAuthor():
    """Funkcja:
        funkcja definująca stan jako stan o autorze"""
    global gameState
    gameState = "author"

def showTopScores():
    """Funkcja:
        funkcja definująca stan jako stan najlepszych wyników"""
    global gameState
    gameState = "topScores"

def quitGame():
    """Funkcja:
        funkcja definująca stan jako stan opuszczenia gry"""
    global gameState
    gameState = "quit"

def backMenu():
    """Funkcja:
        funkcja definująca stan jako stan menu"""
    global gameState
    gameState = "menu"

def Sound():
    """Funkcja:
        funkcja zatrzymująca i uruchamiająca muzykę"""
    if pygame.mixer.music.get_busy():
       pygame.mixer.music.pause()
    else:
       pygame.mixer.music.unpause()


gameState = "menu"                                                              #i dodajemy je do menu
menu = Menu()
menu.addButton(Button("Start", (250, 130), startGame))
menu.addButton(Button("Rules", (250, 210), showRules))
menu.addButton(Button("Author", (250, 290), showAuthor))
menu.addButton(Button("Top Scores", (250, 370), showTopScores))
menu.addButton(Button("Sound", (250, 450), Sound))
menu.addButton(Button("Quit", (250, 530), quitGame))

def getColor():                                                                 #losowanie kolorków dla kształtów
    """Funkcja:
        losująca przypadkowy kolor z podanych odcieni niebieskich"""
    colors = [(185, 237, 221), (135, 203, 185), (86, 157, 170), (87, 125, 134), (121, 224, 238), (152, 238, 204), (48, 162, 255), (0, 196, 255)]
    color = choice(colors)
    return color

figure, nextFigure = deepcopy(choice(figures)), deepcopy(choice(figures))       #aktualna i następna figura i jej kolory
color, nextColor = getColor(), getColor()

score, lines = 0, 0                                                             #punkty i wyeliminowane linie
scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

def checkBorders():                                                             #żeby figury nie mogły wyjść poza granice
    """Funkcja:
        sprawdzająca czy figura nie nachodzi przy ruchu na granice pola/inne figury"""
    if figure[i].x < 0 or figure[i].x > width - 1:
        return False
    elif figure[i].y > height - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True

def readTopScores():                                                            #odczytuje najlepsze wyniki z json
    """Funkcja:
        funkcja odczytująca najlepsze wyniki z pliku json"""
    if os.path.exists("wyniki.json"):
        with open("wyniki.json", "r") as file:
                data = json.load(file)
                wyniki = data["scores"]
    else:
        wyniki = []
    return wyniki

def writeTopScores(score):                                                      #dodaje aktualny wynik do json (o ile jest lepszy niż te co tam są)
    """Funkcja:
        funkcja dodająca aktualny wynik do pliku z najleoszymi (o ile jest lepszy niż aktualne top 5)
    Input:
        score (int) - aktualny wynik"""
    if os.path.exists("wyniki.json"):
        with open("wyniki.json", "r") as file:
            jsonData = file.read()
            data = json.loads(jsonData)
            wyniki = data["scores"]
            wyniki.append(score)
            wyniki.sort(reverse=True)
            wyniki = wyniki[:5]

            with open("wyniki.json", "w") as file:
                data["scores"] = wyniki
                json.dump(data, file)
    else:
        data = {"scores": [score]}
        with open("wyniki.json", "w") as file:
            json.dump(data, file)

while True:                                                                     #zaczynamy gierke

    dx, rotate = 0, False
    screen.blit(background, (0, 0))

    if gameState == "menu":                                                     #otwieramy menu i obsługujemy przyciski
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu.click(event.pos)

        menu.draw(screen)

    elif gameState == "game":                                                   #właściwa gra

        screen.blit(gameScreen, (20, 20))                                       #tworzymy okienko
        gameScreen.blit(gameBackground, (0, 0))
        for i in range(lines):
            pygame.time.wait(200)

        for event in pygame.event.get():                                        #obsługa przycisków
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                elif event.key == pygame.K_DOWN:
                    animLimit = 100
                elif event.key == pygame.K_UP:
                    rotate = True

        figureOld = deepcopy(figure)                                            #przesuwanie prawo/lewo
        for i in range(4):
            figure[i].x += dx
            if not checkBorders():                                              #chyba że wyjdziemy za granice to wraca do poprzedniego położenia
                figure = deepcopy(figureOld)
                break

        animCount += animSpeed
        if animCount > animLimit:                                               #opadanie figury w dół
            animCount = 0
            figureOld = deepcopy(figure)
            for i in range(4):
                figure[i].y += 1
                if not checkBorders():                                          #chyba że opadnie na sam dół to wtedy tworzy nową
                    for i in range(4):
                        field[figureOld[i].y][figureOld[i].x] = color
                    figure, color = nextFigure, nextColor
                    nextFigure, nextColor = deepcopy(choice(figures)), getColor()
                    animLimit = 2000
                    break

        center = figure[0]                                                      #obracanko
        figureOld = deepcopy(figure)                                            #środkiem obrotu jest pierwszy z czterech kwadratów
        if rotate:
            for i in range(4):                                                  #o ile nie ma żadnych kolizji to sie obraca
                x = figure[i].y - center.y
                y = figure[i].x - center.x
                figure[i].x = center.x - x
                figure[i].y = center.y + y
                if not checkBorders():
                    figure = deepcopy(figureOld)
                    break

        line, lines = height - 1, 0                                             #usuwanie pełnych wierszy i dodawanie punktów
        for row in range(height - 1, -1, -1):
            count = 0
            for i in range(width):                                              #count zlicza zajęte pola w każdej linii po kolei
                if field[row][i]:
                    count += 1
                field[line][i] = field[row][i]
            if count < width:                                                   #jeśli nie wszystkie są zajęte to lecimy dalej
                line -= 1
            else:                                                               #ale jeśli tak to wywalamy tą linie i przyspieszamy
                animSpeed += 3
                lines += 1

        score += scores[lines]                                                          #aktualizacja wyniku
        [pygame.draw.rect(gameScreen, (40, 40, 40), iRect, 1) for iRect in grid]        #rysowanko siatki

        for i in range(4):                                                              #rysowanie aktualnej figury
            figureRect.x = figure[i].x * tile
            figureRect.y = figure[i].y * tile
            pygame.draw.rect(gameScreen, color, figureRect)

        for y, raw in enumerate(field):                                                 #rysowanie tych co sobie leżą
            for x, col in enumerate(raw):
                if col:
                    figureRect.x, figureRect.y = x * tile, y * tile
                    pygame.draw.rect(gameScreen, col, figureRect)

        for i in range(4):                                                              #wyświetlanie jaka będzie następna figura
            figureRect.x = nextFigure[i].x * tile + 380
            figureRect.y = nextFigure[i].y * tile + 300
            pygame.draw.rect(screen, nextColor, figureRect)

        rect = pygame.Rect(400, 20, 300, 90)                                            #nazwa gry
        pygame.draw.rect(screen, ("#FFF5B8"), rect)
        text = font.render('TETRIS', True, (0,0,0))
        textRect = text.get_rect(center=rect.center)
        screen.blit(text, textRect)

        rect = pygame.Rect(400, 605, 300, 90)                                           #licznik punktów
        pygame.draw.rect(screen, ("#FFF5B8"), rect)
        text = font.render(f"Score: {score}", True, (0,0,0))
        textRect = text.get_rect(center=rect.center)
        screen.blit(text, textRect)

        rect = pygame.Rect(400, 120, 300, 90)                                           #licznik punktów
        pygame.draw.rect(screen, ("#FFF5B8"), rect)
        text = font.render("Next:", True, (0,0,0))
        textRect = text.get_rect(center=rect.center)
        screen.blit(text, textRect)

        for i in range(width):                                                          #przegrana
            if field[0][i]:
                field = [[0 for _ in range(width)] for _ in range(height)]
                for iRect in grid:
                    pygame.draw.rect(gameScreen, getColor(), iRect)
                    screen.blit(gameScreen, (20, 20))
                    pygame.display.flip()
                    clock.tick(200)
                writeTopScores(score)
                score = 0 
                animCount, animSpeed, animLimit = 0, 60, 2000
                gameState = "menu"
        
        clock.tick(fps)
        pygame.display.flip()

    elif gameState == "rules":                                                          #stronka z zasadami gry

        gameScreen.blit(gameBackground, (0, 0))

        rect = pygame.Rect(50, 50, 400, 90)                                             #tytuł stronki
        pygame.draw.rect(screen, ("#FFF5B8"), rect)
        text = font.render("Rules of the Game:", True, (0, 0, 0))
        textRect = text.get_rect(center=rect.center)
        screen.blit(text, textRect)

        rect1 = pygame.Rect(50, 150, 620, 380)                                          #treść stronki
        pygame.draw.rect(screen, ("#FFF5B8"), rect1)

        text1 = miniFont.render("Celem gry jest usunięcie jak największej liczby figur", True, (0, 0, 0))
        textRect1 = text1.get_rect(center=(360, 200))
        screen.blit(text1, textRect1)

        text2 = miniFont.render("pojawiających się na ekranie w różnych kształtach.", True, (0, 0, 0))
        textRect2 = text2.get_rect(center=(360, 235))
        screen.blit(text2, textRect2)

        text3 = miniFont.render("Figury można obracać za pomocą strzałki w górę,", True, (0, 0, 0))
        textRect3 = text3.get_rect(center=(360, 270))
        screen.blit(text3, textRect3)

        text4 = miniFont.render("przesuwać za pomocą strzałek w lewo i prawo oraz", True, (0, 0, 0))
        textRect4 = text4.get_rect(center=(360, 305))
        screen.blit(text4, textRect4)

        text5 = miniFont.render("przyspieszyć opadanie za pomocą strzałki w dół.,", True, (0, 0, 0))
        textRect5 = text5.get_rect(center=(360, 340))
        screen.blit(text5, textRect5)

        text6 = miniFont.render("By usunąć kolejne figury należy zapełnić poziomo całą linię.", True, (0, 0, 0))
        textRect6 = text6.get_rect(center=(360, 375))
        screen.blit(text6, textRect6)

        text7 = miniFont.render("Punktacja:", True, (0, 0, 0))
        textRect7 = text7.get_rect(center=(360, 440))
        screen.blit(text7, textRect7)

        text8 = miniFont.render("1 linia na raz - 100p; 2 - 300p; 3 - 700p; 4 - 1500p", True, (0, 0, 0))
        textRect8 = text8.get_rect(center=(360, 470))
        screen.blit(text8, textRect8)

        rulesMenu = Menu()                                                              #żeby jak klikniemy X to wyszło
        rulesMenu.addButton(Button("Back", (250, 600), backMenu))                       #a jak back to powróciło do menu

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rulesMenu.click(event.pos)

        rulesMenu.draw(screen)

        pygame.display.flip()

    elif gameState == "author":                                                         #w sumie to tak samo jak w tym z zasadami

        gameScreen.blit(gameBackground, (0, 0))
        
        rect = pygame.Rect(50, 50, 200, 90)
        pygame.draw.rect(screen, ("#FFF5B8"), rect)
        text = font.render("Author:", True, (0, 0, 0))
        textRect = text.get_rect(center=rect.center)
        screen.blit(text, textRect)

        rect1 = pygame.Rect(50, 150, 620, 380)
        pygame.draw.rect(screen, ("#FFF5B8"), rect1)

        text1 = miniFont.render("Jestem Magda, jestem studentką pierwszego roku", True, (0, 0, 0))
        textRect1 = text1.get_rect(center=(360, 200))
        screen.blit(text1, textRect1)

        text2 = miniFont.render("Matematyki Stosowanej na Politechnice Wrocławskiej.", True, (0, 0, 0))
        textRect2 = text2.get_rect(center=(360, 230))
        screen.blit(text2, textRect2)

        text3 = miniFont.render("Do napisania gry zainspirowała mnie lista 6 profesora", True, (0, 0, 0))
        textRect3 = text3.get_rect(center=(360, 280))
        screen.blit(text3, textRect3)

        text4 = miniFont.render("Szwabińskiego, ponieważ głupio byłoby nic nie oddać.", True, (0, 0, 0))
        textRect4 = text4.get_rect(center=(360, 310))
        screen.blit(text4, textRect4)

        text5 = miniFont.render("Coś tu chyba jeszcze powinnam napisać ale szczerze", True, (0, 0, 0))
        textRect5 = text5.get_rect(center=(360, 360))
        screen.blit(text5, textRect5)

        text6 = miniFont.render("nie mam pomysłu co, więc mam nadzieje, że tyle wystarczy", True, (0, 0, 0))
        textRect6 = text6.get_rect(center=(360, 390))
        screen.blit(text6, textRect6)

        authorMenu = Menu()
        authorMenu.addButton(Button("Back", (250, 600), backMenu))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        authorMenu.click(event.pos)

        authorMenu.draw(screen)

        pygame.display.flip()

    elif gameState == "topScores":                                                  #też jak w tym z zadadami

        topScores = readTopScores()

        gameScreen.blit(gameBackground, (0, 0))
        
        rect = pygame.Rect(50, 50, 300, 90)
        pygame.draw.rect(screen, ("#FFF5B8"), rect)
        text = font.render("Top 5 scores:", True, (0, 0, 0))
        textRect = text.get_rect(center=rect.center)
        screen.blit(text, textRect)

        rect1 = pygame.Rect(50, 150, 300, 380)
        pygame.draw.rect(screen, ("#FFF5B8"), rect1)

        y = 150                                                                     #z tą różnicą że cyferki i wyniki dodajemy w pętli po kolei w równych odstępach
        for wynik in topScores:
            text = font.render(f"{wynik}", True, pygame.Color("black"))
            screen.blit(text, (150, y))
            y += 70

        y1 = 150
        for i in range(5):
            text = font.render(f"{i+1}.", True, pygame.Color("black"))
            screen.blit(text, (100, y1))
            y1 += 70

        scoresMenu = Menu()
        scoresMenu.addButton(Button("Back", (250, 600), backMenu))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        scoresMenu.click(event.pos)

        scoresMenu.draw(screen)

        pygame.display.flip()

    elif gameState == "quit":
        exit()

    pygame.display.flip()