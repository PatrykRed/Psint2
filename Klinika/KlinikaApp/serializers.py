from rest_framework import serializers
from .models import Uzytkownik, Zwierze, Lekarz, Operacje, Wizyty, Recepty

class UzytkownikSerializer(serializers.ModelSerializer):

    class Meta:
        model = Uzytkownik
        fields = ['id_Uzytkownik', 'Imie', 'Nazwisko', 'Login', 'Haslo', 'Mail']

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Uzytkownik = validate_data.get('id_Uzytkownik', instance.id_Uzytkownik)
        instance.Imie = validate_data.get('Imie', instance.imie)
        instance.Nazwiwsko = validate_data.get('Nazwisko', instance.nazwisko)
        instance.Login = validate_data.get('Login', instance.login)
        instance.Haslo = validate_data.get('Haslo', instance.Haslo)
        instance.Mail = validate_data.get('Mail', instance.Mail)
        instance.save()

        return instance

class ZwierzeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zwierze
        fields = ['id_Zwierze', 'Imie', 'Rasa', 'Uzytkownik_id_Uzytkownik']

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Zwierze = validate_data.get('id_Zwierze', instance.id_Zwierze)
        instance.Imie = validate_data.get('Imie', instance.imie)
        instance.Rasa = validate_data.get('Rasa', instance.Rasa)
        instance.Uzytkownik_id_Uzytkownik = validate_data.get('Uzytkownik_id_Uzytkownik', instance.Uzytkownik_id_Uzytkownik)
        instance.save()

        return instance

class OperacjeSerializer(serializers.ModelSerializer):

    model = Operacje
    fields = ['id_Operacje', 'Nazwa', 'Data', 'Zwierze_id_Zwierze']

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Operacje = validate_data.get('id_Operacje', instance.id_Operacje)
        instance.Nazwa = validate_data.get('Nazwa', instance.Nazwa)
        instance.Data = validate_data.get('Data', instance.Data)
        instance.Zwierze_id_Zwierze = validate_data.get('Zwierze_id_Zwierze', instance.Zwierze_id_Zwierze)
        instance.save()

        return instance

class LekarzSerializer(serializers.ModelSerializer):

    model = Lekarz
    fields =['id_Wizyty', 'Data', 'Zwierze_id_Zwierze', 'Lekarz_id_Lekarz', 'Operacje_id_Operacje']

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Wizyty = validate_data.get('id_Wizyty', instance.id_Wizyty)
        instance.Data = validate_data.get('Data', instance.Data)
        instance.Zwierze_id_Zwierze = validate_data.get('Zwierze_id_Zwierze', instance.Zwierze_id_Zwierze)
        instance.Lekarz_id_Lekarz = validate_data.get('Lekarz_id_Lekarz', instance.Lekarz_id_Lekarz)
        instance.Operacje_id_Operacje = validate_data.get('Operacje_id_Operacje', instance.Operacje_id_Operacje)
        instance.save()

        return instance

class WizytySerializers(serializers.ModelSerializer):

    model = Wizyty
    fields = ['id_Wizyty','Data', 'Zwierze_id_Zwierze',' Lekarz_id_Lekarz' ]

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Wizyty = validate_data.get('id_Wizyty', instance.id_Wizyty)
        instance.Data = validate_data.get('Data', instance.Data)
        instance.Zwierze_id_Zwierze = validate_data.get('Zwierze_id_Zwierze', instance.Zwierze_id_Zwierze)
        instance.Lekarz_id_Lekarz = validate_data.get('Lekarz_id_Lekarz', instance.Lekarz_id_Lekarz)
        instance.save()

        return instance

class ReceptySerializers(serializers.ModelSerializer):
    model = Recepty
    fields =['id_Recepty', 'Nazwa_Recepty', 'Opis', 'Lekarz_id_Lekarz']

    def Create(self, Validate_data):
        return UzytkownikSerializer(**Validate_data)

    def Update(self, instance, validate_data):
        instance.id_Recepty = validate_data.get('id_Recepty', instance.id_Recepty)
        instance.Nazwa_Recepty = validate_data.get('Nazwa_Recepty', instance.Nazwa_Recepty)
        instance.Opis = validate_data.get('Opis', instance.Opis)
        instance.Lekarz_id_Lekarz = validate_data.get('Lekarz_id_Lekarz', instance.Lekarz_id_Lekarz)
        instance.save()

        return instance
