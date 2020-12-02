def liczba_liter(zmienna, litera):
    return zmienna.count(litera)

def zad2():
    zmienna = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
    imie_string = 'Patryk'
    nazwisko_string = 'Redykiert'
    imie = list(imie_string)
    nazwisko = list(nazwisko_string)
    litera_1 = liczba_liter(zmienna, imie[2])
    litera_2 = liczba_liter(zmienna, nazwisko[3])
    print("W tekście jest {} liter ... oraz {} liter ...".format(litera_1,litera_2))
#zad2()
def zad3():
    tekst = 'Jestem dobry z programowania'
    liczba = 3.141592653589793
    liczba2 = 23
    liczba3 = -23
    print('{:^33}'.format(tekst))
    print('{:10.5}'.format(tekst))
    print('{:06.2f}'.format(liczba))
    print('{: =+5d}'.format(liczba2))
    print('{: =5d}'.format(liczba3))

#zad3()

def zad4():
    tekst = 'Uczę sie programować'
    print(dir(tekst))
    help(tekst.endswith("ok") )

#zad4()

def zad5():
    tekst = 'Patryk Redykiert'[::-1]
    print(tekst)
#zad5()

def zad6():
    Lista=[1,2,3,4,5,6,7,8,9,10]
    Lista2=[]
    for i in range(1, 11):
        if (i > 5):
            Lista.pop()
            Lista2.append(i)
    print(Lista2)
#zad6()

def zad7():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [6, 7, 8, 9, 10]
    lista_połączona = []
    lista_połączona_kopia= []
    for licznik in range(10):
        if(licznik<5):
            lista_połączona.append(str(lista1[licznik]))
        else:
            lista_połączona.append(str(lista2[licznik-5]))
    for licznik in range(10):
        lista_połączona[licznik]=int(lista_połączona[licznik])

    lista_połączona = [0] + lista_połączona
    lista_połączona_kopia = lista_połączona

    for licznik in range(11):
        print(lista_połączona[10-licznik], end=" ")

#zad7()

def zad8():
    krotka =(123456,135790,234123,432123,'Adam Nowak','Jan Kowalski','Dawid Borawski','Damian Stonoga')
    krotka1 = krotka[0:4]
    krotka2 = krotka[4:8]
    print(krotka1)
    print(krotka2)
    krotka_studenta1 = krotka[0:1] + krotka[4:5]
    print(krotka_studenta1)
    krotka_studenta2 = krotka[1:2] + krotka[5:6]
    print(krotka_studenta2)
    krotka_studenta3 = krotka[2:3] + krotka[6:7]
    print(krotka_studenta3)
    krotka_studenta4 = krotka[3:4] + krotka[7:8]
    print(krotka_studenta4)
#zad8()

def zad9():
    studenci = {
        123456: (21, "adam@domena.pl", 1999, "Olsztyn ul Słoneczna 20"),
        135790: (21, "jan@domena.pl", 1999, "Mrągowo ul. Żabia 74"),
    }
    print(studenci[123456])
#zad9()
def zad10():
    numery = [111999111,111999111,111999111,111999112,111999113,111999188,111999100, 111999100]
    numery = set(numery)
    print(numery)
#zad10()

def zad11():
    wypisz = ""
    for i in range(1, 11):
       print(i)

#zad11()
def zad12():
    for i in range(100, -21, -5):
        print(i)

#zad12()