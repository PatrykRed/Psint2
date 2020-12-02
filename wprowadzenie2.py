#zad1
def zad1(a_list, b_list):
    return [i for i in a_list if i % 2 == 0] + [i for i in b_list if i % 2 == 1]
#print(zad1([0,1,2,3], [5,6,7,8]))

#zad2
def zad2(txt):
    slownik = {
        'length': len(txt),
        'letters': [char for char in txt],
        'big_letters': txt.upper(),
        'small_letters': txt.lower()
    }
    return slownik

#slownik = zad2("Ala ma kota")
#print(slownik['letters'])

#zad3
def zad3(letter, text):
    return text.replace(letter, "")

#print(zad3('a',"tekst"))

#zad4
def zad4(type, temp):
    if type == 'K':
        return 273.15 + temp
    elif type == 'R':
        return (temp + 273.15) * 1.8
    elif type == 'F':
        return (temp * 1.8) + 32
    else:
        return "Nieprawidłowy typ"

#print(zad4('F',50))


#zad5
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dodawanie(self,a,b):
        return a + b

    def odejmowanie(self,a,b):
        return a - b

    def mnozenie(self,a,b):
        return a * b

    def dzielenie(self,a,b):
        return a / b

#Calculator=Calculator(8,5)
#print(Calculator.dodawanie(8,5))
#print(Calculator.odejmowanie(8,5))
#print(Calculator.mnozenie(8,5))
#print(Calculator.dzielenie(8,5))

#zad6

class scienceCalculator(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def potegowanie(self,a):
        self.a = a
        
#scienceCalculator =scienceCalculator(8,5)
#print(scienceCalculator.potegowanie(8))
#print(scienceCalculator.dzielenie(8,5))

#zad7
def odwrot():
    tekst = input()
    return tekst[::-1]


#print(odwrot())

# zad8

class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name


    def FileRead(self,file_name):


    def update_file(self,file_name):
        plik = open(self.file_name + ".txt", "a")
        plik.write('text_data')
        plik.close()




FileManager = FileManager('plik.txt')
print(FileManager.FileRead('plik.txt'))