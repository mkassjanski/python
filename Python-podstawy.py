#Utworz zmienne z wynikiem gracza 1 oraz z gracza 2.
#Zdefiniuj lancuch spacja (zawieraj  spacje). Zdefiniuj jedna
#zmienna wyniki wyswietlajac wynik gracza 1 i gracza 2.
#Wyniki gracza 1 i 2 maja byc wyswietlone wierszach pod soba i
#maja sie zaczynac 10 spacji od lewego marginesu.
#wynik1=100
#wynik2=153
#spacja=" "
#info='''%sWynik pierwszego gracza %s.
#%sWynik drugiego gracza %s '''
#print(info %(spacja*10,wynik1,spacja*10,wynik2))

#Utworz piecioelementow liste zakupow. Wyswietl
#cala liste, tylko trzeci element listy, wszystkie elementy bez
#pierwszego i ostatniego.
#zakupy = ["mleko", "chleb", "cukier", "sol", "woda"]
#print(zakupy)
#print(zakupy[2])
#print(zakupy[1:4])

#Zadanie Dodaj dwa produkty do swojej listy oraz usun
#pierwszy i trzeci element z listy.
#zakupy = ["mleko", "chleb", "cukier", "sol", "woda"]
#zakupy.append("maslo")
#zakupy.append("margaryna")
#print(zakupy)
#del zakupy[0]
#del zakupy[1]
#print(zakupy)

#Zadanie Utworz lista1=[1,3,5], lista2=[2,4,6],
#lista3 = lista1 + lista2 i lista4 = 3*lista1. Wyswietl te listy.
#lista1=[1,3,5]
#lista2=[2,4,6]
#lista3 = lista1 + lista2
#lista4 = 3*lista1
#print(lista3)
#print(lista4)

#Zadanie Napisac program w ktorym definiuje sie zmienna
#Liczba_zyc = 3. Nastepnie jesli zmienna jest wieksza od 0 to
#sie od niej odejmuje 1 i wyswietla sie jej wartosc.
#Licza_zyc=3
#if(Licza_zyc>0):
#    Licza_zyc=Licza_zyc-1
#    print(Licza_zyc)

#Zadanie Napisac program w ktorym definiuje sie zmienna
#Liczba_zyc = 3. Nastepnie jesli zmienna jest wieksza od 0 to
#sie od niej odejmuje 1 i wyswietla sie jej wartosc w przeciwnym
#razie wyswietla sie komunikat Koniec gry. Skopiuj i zastosuj
#instrukcje kilka razy.
#Licza_zyc=3
#if(Licza_zyc>0):
#    Licza_zyc=Licza_zyc-1
#    print(Licza_zyc)
#else:
#    print("Koniec gry")

#Zadanie Zdefiniuj zmienna kolor zawierajaca lancuch
#czerwony. Napisz instrukcje, ktora jesli zmienna kolor zawiera
#czerwony to zmienia kolor na zielony i go wyswietla, jesli kolor
#niebieski to zmienia na zielony i wyswietla, w przeciwnym razie
#zmienia kolor na niebieski i wyswietla. Wykonaj kilka razy te
#instrukcje.
#kolor="niebieski"
#if(kolor=="czerwony"):
#    kolor="zielony"
#    print(kolor)
#elif(kolor=="niebiski"):
#    kolor="zielony"
#    print(kolor)
#else:
#    kolor="niebieski"
#    print(kolor)

#Zadanie Napisac program w ktorym definiuje sie zmienna
#monety oraz instrukcje, ktora wyswietla komunikat calkiem
#niezle, jesli 100 <=monety<=200. Uruchom program dla kilku
#wartosci monety.
#monety=34
#if(monety>=100 and monety<=200):
#    print("Calkiem niezle")

#Zadanie Napisac program w ktory definiuje sie zmienna x oraz
#instrukcje, ktora bedzie wyswietlala komunikat x nie jest cyfra,
#jesli zmienna x nie bedzie cyfra.
#x=5
#if(type(x) is int):
#    if(x>=0 and x<=9):
#        print("to jest cyfra")
#    else:
#        print("x nie jest cyfra")
#else:
#    print("x nie jest cyfra")

#Zadanie Zdefiniuj zmienna wiek jako lancuch zawierajacy twoj
#wiek (zapisany cyframi). Wymysl instrukcje, ktora w warunku
#bedzie zawierala twoj wiek, ale uzyty jako liczbe.
#wiek=17
#if(int(wiek)>=18):
#    print("Jestes pelnoletni")
#else:
#    print("Dzieciak")

#Zadanie Napisac program, ktory wczyta od uzytkownika
#pewien napis, a nastepnie wyswietli 30 kopii tego napisu, kazda
#w osobnej linii.
#napis = raw_input("Podaj cos")
#print((napis+"\n")*30)

#Zadanie Napisac program, ktory po wprowadzeniu dlugosci
#podstawy i wysokosci trojkata, obliczy jego pole
#a = raw_input("Podstawa")
#h = raw_input("Wysokosc")
#print(float((int(a)*int(h))/2))


#Zadanie Napisac program, ktory wypisze:
#a) kwadraty wszystkich liczb calkowitych od 0 do 20,
#b) szesciany wszystkich liczb calkowitych od 10 dp 20,
#c) odwrotnosci wszystkich parzystych liczb calkowitych od 16
#do 6 (w podanej kolejnosci).

#for i in range(0,21):
#    print(pow(i,2))

#for i in range(10,21):
#    print(pow(i,3))

#for i in range(16,5,-2):
#    print(pow(i,-1))


#Zadanie Napisac program, ktory bedzie wypisywal cyfre
#jednostek, dziesitek i setek liczby z zakresu od 0 do 999.
#Liczbe ma wprowadzac uzytkownik programu. Wyniki i napisy
#nalezy rozmiescic w odpowiednich kolumnach.

#a = raw_input("Liczba")
#setki=int(a)/100
#a2=int(a)-setki*100
#dzisiatki=a2/10
#a3=a2-dzisiatki*10
#print(a)
#print("Setki: %4i Dzisiatki: %4i Jednosci: %4i" % (setki,dzisiatki,a3))

#Zadanie Napisac program, ktory po wprowadzeniu przez
#uzytkownika dwoch liczb calkowitych z zakresu od 0 do 100
#beedzie wyswietlal ich srednia kwadratowa, arytmetyczna,
#geometryczna i harmoniczna. Kazda srednia ma byc
#wyswietlona w osobnym wierszu wraz z jej nazwa oraz z jakich
#liczb byla liczona. Dokladnosc wynikow nalezy ustawic na dwa
#miejsca po przecinku. Wyniki i napisy nalezy rozmiescicw
#odpowiednich kolumnach.
#import math
#aa = raw_input("Liczba 1:")
#bb = raw_input("Liczba 1:")
#
#a=float(aa)
#b=float(bb)
#
#kwadratowa=math.sqrt((pow(a,2)+pow(b,2))/2)
#arytemtyczna=(a+b)/2
#geometryczna=math.sqrt(a*b)
#harmoniczna=2/(1/a+1/b)
#print("Srednia kwadratowa liczb %2i i %2i jest rowna %5.2f" %(a,b,kwadratowa))
#print("Srednia arytemetyczna liczb %2i i %2i jest rowna %5.2f" %(a,b,arytemtyczna))
#print("Srednia geometryczna liczb %2i i %2i jest rowna %5.2f" %(a,b,geometryczna))
#print("Srednia harmoniczna liczb %2i i %2i jest rowna %5.2f" %(a,b,harmoniczna))

#Zadanie Zmodyfikuj powyzszy program w ten sposob, aby
#wyswietlal imiona z listy a oraz z ilu liter sie skladaja

#a = ["Ala", "Ela", "Adam", "Janek"]
#for i in range(len(a)):
#    print(i, a[i], len(a[i]))

#l1=["a", "b", "c"]
#l2=["d", "e"]
#for x in l1:
#    for y in l2:
#        print(x, y)
#        print(y, x)

#print("To ja:")
#print("a","d")
#print("d","a")
#print("a","e")
#print("e","a")
#print("b","d")
#print("d","b")
#print("b","e")
#print("e","b")
#...

#Zadanie a)Uzywajac m.in. polecen: range, continue i % napisz
#program wyznaczajacy kwadraty wszystkich liczb naturalnych
#od 0 do 100 niepodzielnych przez 6.
#b) Uzywajac m.in. polecen: range, continue, % oraz not napisz
#program wyznaczajacy kwadraty wszystkich liczb naturalnych
#od 1 do 1000 podzielnych przez 25

#for i in range(0,101):
#    if(i%6==0):
#        continue
#    print(pow(i,2))

#for i in range(1,1001):
#    if(not i%25==0):
#        continue
#    print(pow(i,2))

#Zdefiniuj funkcje:
#def pierw(n):
#    return n**0.5
#oraz za jej pomoca oblicz sqrt z 2
#print(pierw(2))

#Zadanie Napisac funkcje, ktora bedzie liczyla sume
#odwrotnosci dwoch liczb. W przypadku, gdy co najmniej jedna
#z liczb jest zerem ma sie pojawiac stosowny komunikat.

#def suma(a,b):
#    if(a==0 or b==0):
#        print("Jedna z liczb jest zerem")
#    else:
#        print(pow(a,-1)+pow(b,-1))

#suma(2,0)

#def suma(*arg):
#    s=0
#    for x in arg:
#        s=s+x
#    return s

#print(suma(*range(10)))

#
#def silnia(n):
#    if n>1:
#        return n*silnia(n-1)
#    else:
#        return 1

#print(silnia(5))

#import sys
#print("Podaj dlugosc boku kwadratu i wcisnij enter")
#a=int(sys.stdin.readline())
#print("Pole kwadratu o boku", a, "wynosi", a**2)

#Zadanie Przetestowac dzialenie tego programu. Znalezc
#przynajmniej dwa rozne przypadki w ktorych program nie dziala
#poprawnie. Zmodyfikowac program, aby dzialal rowniez
#poprawnie w tych znalezionych przypadkach.
#odp: wartosci ujemne i wartosc z przecinkami
#import sys
#print("Podaj dlugosc boku kwadratu i wcisnij enter")
#a=float(sys.stdin.readline())
#if(a<=0):
#    print("Dlugosc boku musi byc wieksza od 0")
#else:
#    print("Pole kwadratu o boku", a, "wynosi", a**2)
import sys
#a=int(sys.stdin.readline())
#b=int(sys.stdin.readline())
#r=0
#def nwd(a,b):
#    while(b!=0):
#        r=a%b
#        a=b
#        b=r
#    print(a)
#    return a

#def nww(a,b):
#    k=a*b
#    nwdd=nwd(a,b)
#    return k/nwdd

#nwd(34.0,23.0)
#nww(12.0,16.0)

##############
##SORTOWANIE##
##############

#import sys
#a=[]
#print("Ile elementow bedzie miala lista?")
#n=int(sys.stdin.readline())
#def czytaj():
#    for i in range(n):
#        print("Podaj",i,"element listy")
#        a.append(float(sys.stdin.readline()))
#    return a


#print("Lista: ", czytaj())
#print("Najmniejszy element listy: ", min(a))
#print("Najwiekszy element listy: ", max(a))

#def zamiana(a,k,l):
#    t=a[k]
#    a[k]=a[l]
#    a[l]=t
#    return a

#def sortow(a,n):
#    for i in range(n-1):
#        minn=i
#        for j in range(i+1,n):
#            if a[j]<a[minn]:
#                minn=j
#                zamiana(a,minn,i)
#    return a

#print(sortow(a,n))

###########################
#Python-funkcje losujace###
###########################

import random
#liczba=random.randint(1,128)
#print("Zgadnij liczbe naturalna z zakresu od 1 do 128")
#while True:
#    strzal=input()
#    i=int(strzal)
#    if(strzal==liczba):
#        print("Zgadlem")
#        break
#    elif(strzal<liczba):
#        print("Szukana liczba jest wieksza")
#    elif(strzal>liczba):
#        print("Szukana liczba jest mniejsza")

#tab=[1,2,3,3,4,4,4,4]

#liczba=random.choice(tab)
#while True:
#    strzal=input()
#    i=int(strzal)
#    if(strzal==liczba):
#         print("Zgadlem")
#         break
#    elif(strzal<liczba):
#        print("Szukana bramka jest wieksza")
#    elif(strzal>liczba):
#       print("Szukana bramka jest mniejsza")
