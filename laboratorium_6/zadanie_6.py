#Zadanie 6. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2,3,5.
#Jedynka też jest taką liczbą.
#Napisz program który wylicza ile takich liczb znajduje się w przedziale od 1 do N włącznie, gdzie N jest wczytywane.
#Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
#Należy obsłużyć wyjątek wczytania danej niebędącą liczbą naturalną.

#Określamy zmienne
a = 1
suma = 1
flag = True

#Wstawiamy pętlę by program nie wyłączał się po jednej liczbie
while a == 1:
    while flag == True:
        #Program wysyła zapytanie o zakres (liczbę N)
        #Program tylko zaakceptuje liczbę naturalną +
        #W innym wypadku program nie zakończy się, tylko będzie wysyłał ponowne zapytania o wpisanie poprawnej liczby
        try:
            N = int(input('Podaj liczbę: '))
            if N > 0:
                print('liczba jest naturalna')
                flag = False
            else:
                raise ValueError
        except ValueError:
            print('liczba nie jest naturalna')
    print('Liczby 2,3,5-kowe z zakrestu to: 1')
    #Część programu w którym wyszukujemy liczby zgodne z założeniem
    #Program sprawdza każdą liczbę pomiędzy 2 a N (wraz z N)
    for i in range(2, N + 1):
        k = 2
        l = i
        #Każda liczba z zakresu jest dzielona przez 2,3,4 (nie jest to potrzebne ale nie jestem pewien jak to ominąć),5
        #tak długo jak jest to możliwe
        #Gdy liczba nie jest możliwa do podzielenia kończy się pętla dla danej liczby
        #Jeżeli składała się tylko z czynników 2,3,5  i = 1 a wartość zmiennej odpowiadającej za sumę takich liczb powiększy się o 1
        while i >= 1 and k != 6:
            if i % k == 0:
                i = i / k
            else:
                k += 1
        if i == 1 and k == 6:
            suma += 1
            print(l)

    print('W podanym przedziale występuje ',suma,' takich liczb')
    flag = True
    suma = 1

# Przypadki testowe :
# N = 20  suma = 14
# N = 50  suma = 24
# N = 500  suma = 67
# N = 1 000 000  suma = 507