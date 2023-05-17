def check(text):

    """Funkcja
        funkcja sprawdza poprawność użycia nawiasów w podanym tekście
    Input:
        text (str) - tekst do sprawdzenia
    Output:
        True/False (bool) - funkcja zwraca true jeśli wszystkie nawiasy zostały użyte poprawnie"""

    nawiasy = []

    for znak in text:
        if znak in "({[<":                                       #tworzymy liste wszystkich nawiasów lewych
            nawiasy.append(znak)
    
    for i in range(len(nawiasy)):                               #sprawdzamy czy w liście nawiasów przednich nie ma sytacji gdzie obok siebie są dwa takie same nawiasy
            if i > 0 and nawiasy[i-1] == nawiasy[i]:            #nie musimy sprawdzać tego dla tylnich bo jeśli dla przednich nie ma a dla tylnich by była to i tak w dalszym sprawdzaniu wyjdzie błąd w ilości nawiasów lub przy ich kolejności
                return False
            
    for znak in text:

        if znak in ")}]>":

            if not nawiasy:                                     #jeśli znaleźliśmy jakiś nawias prawy a lista tych lewych jest pusta to coś jest nie tak             
                return False
            
            if znak == ")" and nawiasy[-1] != "(":              #sprawdzamy czy znaleziony nawiast prawy jest taki sam jak ostatni na liście nawiast lewych (żeby były w dobrej kolejności)
                return False
            if znak == "}" and nawiasy[-1] != "{":
                return False
            if znak == "]" and nawiasy[-1] != "[":
                return False                                    
            nawiasy.pop()                                       #jeśli wszystko sie zgadza to usuwamy ostatni nawias z listy nawiasów lewych
    

    return not nawiasy                                          #jeśli wszystkie nawiasy były ustawione poprawnie to ostatecznie lista powinna być pusta

print(check("<8*{2*[(5+8)**3]}>"))              #poprawne
print(check("<8*[2*[(5+8)**3]]>"))              #dwa takie same nawiasy obok siebie
print(check("<8*{2*[{5+8]**3]}>"))              #niepasujące nawiasy
print(check("<8*2*[(5+8)**3]}>"))               #za mało nawiasów lewych
print(check("<8*{2*[(5+8)**3}>"))               #za mało nawiasów prawych
print(check("<{(})>"))
print(check("{a[b(c)d]}"))                      #poprawnie z literkami