a = int(input("Podaj liczbę:    "))

b = 1
c = 1
wynik = 1

for i in range(a-1):
    b = wynik
    wynik += c
    c = b

print(wynik)