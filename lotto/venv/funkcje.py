import random
import time

random.seed(time.time())

def convertIntoInt(otrzymaneLiczby):
    listaLiczbZnaki = otrzymaneLiczby.split(' ')
    liczby = []
    for i in listaLiczbZnaki:
        liczby.append(int(i))
    liczby.sort()
    return liczby

def ileLiczb(liczby):
    n = 0
    for i in liczby:
        n += 1
    return n

def czyRozne(liczby):
    for i in range(0,5):
        for j in range(i+1,6):
            if i != j and liczby[j] == liczby[i]:
                return False
    return True

def sprZakres(liczby):
    checker = 0
    for i in range(0,6):
        if liczby[i] < 1:
            print("Liczba {0} jest poniżej dopuszczalnego zakresu!".format(liczby[i]))
            checker += 1
        elif liczby[i] > 49:
            print("Liczba {0} jest powyżej dopuszczalnego zakresu (1-49)!".format(liczby[i]))
            checker += 1
    if checker > 0:
        return False
    return True