import networkx as nx
import matplotlib.pyplot as plt
import random

def agent(n = 6, prob = 0.4, steps = 10):

    """Funkcja:
        funkcja tworząca grafy ze zmieniającymi miejsce agenatmi????
    Input:
        n (int) - liczba miejsc
        prob (float) - prawdopodobieństwo połączenia między dwoma miejscami
        steps (int) - ilość przejść"""

    graph = nx.gnp_random_graph(n, prob)                        #nasz śliczny randomowy graf
    currentPlace = random.choice(list(graph.nodes()))           #i aktualne miejsce pobytu agenta
    position = nx.spring_layout(graph)                          #oraz ułożenie tych grafów na wykresie żeby nam sie nie przemieszczały potem

    for i in range(steps):
        
        currentPlace = random.choice(list(graph.neighbors(currentPlace)))               #wybieramy randomowo nowe miejsce wśród sąsiadów starego
        plt.figure()                                                                    #tworzymy z grafu wykresik gdzie aktualne miejsce ma inny kolor niż reszta
        nx.draw(graph, pos=position, node_color=['dodgerblue' if el == currentPlace else 'powderblue' for el in graph.nodes()])
        plt.savefig(f"graf_{i}.png")                                                    #i zapisujemy obrazek

agent()

from PIL import Image

def gif(steps = 10):

    """Funkcja:
        funkcja tworzy gifa z utworzonych wcześniej grafów
    Input:
        steps (int) - ilość przejść"""

    files = [f"graf_{i}.png" for i in range(steps)]                                     #zbieramy nazwy wszystkich grafów
    graphs = []

    for graph in files:                                                                 #tworzymy liste z tymi wszystkimi grafami
        graphs.append(Image.open(graph).convert('RGB'))

    graphs[0].save("animacja.gif", format='GIF', append_images=graphs[1:], save_all=True, duration=400)

gif()