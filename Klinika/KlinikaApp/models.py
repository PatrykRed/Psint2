from django.db import models

class Uzytkownik(models.Model):
    id_Uzytkownik = models.IntegerField(null=False)
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Login = models.CharField(max_length=45)
    Haslo = models.CharField(max_length=45)
    Mail = models.CharField(max_length=45)

class Zwierze(models.Model):
    id_Zwierze = models.IntegerField(null=False)
    Imie = models.CharField(max_length=45)
    Rasa = models.CharField(max_length=45)
    Uzytkownik_id_Uzytkownik = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE, null=False)

class Operacje(models.Model):
    id_Operacje = models.IntegerField()
    Nazwa = models.CharField(max_length=45)
    Data = models.DateField(null=False)
    Zwierze_id_Zwierze = models.ForeignKey(Zwierze,on_delete=models.CASCADE,null=False)

class Lekarz(models.Model):
    id_Lekarz = models.IntegerField()
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Specjalizacja = models.CharField(max_length=45)
    Operacje_id_Operacje = models.ForeignKey(Operacje,on_delete=models.CASCADE,null=False)

class Wizyty(models.Model):
    id_Wizyty = models.IntegerField(null=False)
    Data = models.DateField(null=False)
    Zwierze_id_Zwierze = models.ForeignKey(Zwierze,on_delete=models.CASCADE,null=False)
    Lekarz_id_Lekarz = models.ForeignKey(Lekarz,on_delete=models.CASCADE, null= False)

class Recepty(models.Model):
    id_Recepty = models.IntegerField(null=False)
    Nazwa_Recepty = models.CharField(max_length=45)
    Opis = models.CharField(max_length=45)
    Lekarz_id_Lekarz = models.ForeignKey(Lekarz, on_delete=models.CASCADE,null=False)



