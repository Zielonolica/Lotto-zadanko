import funkcje

game = True

while (True):
  otrzymaneLiczby = input("Wybierz 6 różnych liczb z zakresu od 1 do 49 oddzielając je spacjami:\n")

  #zamiana stringa na liste intów
  liczby = funkcje.convertIntoInt(otrzymaneLiczby)

  #czy podano 6 liczb
  if funkcje.ileLiczb(liczby) > 6:
    print("Podano za dużo liczb!")
    continue
  elif funkcje.ileLiczb(liczby) < 6:
    print("Podano za mało liczb!")
    continue

  #czy podane liczby się nie powtarzają
  if funkcje.czyRozne(liczby) == False:
      print("Podane liczby się powtarzają!")
      continue

  #czy wszystkie licizby są od 1 do 49
  if funkcje.sprZakres(liczby) == False:
      continue

  print("wszystko ok")