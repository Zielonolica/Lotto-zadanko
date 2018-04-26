import random
import time

def convertIntoInt(otrzymaneLiczby):
    listaLiczbZnaki = otrzymaneLiczby.split(' ')
    liczby = []
    for i in listaLiczbZnaki:
        liczby.append(int(i))
    liczby.sort()
    return liczby

def czyRozne(liczby):
    for i in range(1,6):
        if liczby[i] == liczby[i-1]:
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

def losowanie():
    random.seed(time.time())
    lotto = random.sample(range(1,50),6)
    lotto.sort()
    return lotto

def checkWin(liczby, lotto):
    for i in range(6):
        if liczby[i] != lotto[i]:
            return False
    return True