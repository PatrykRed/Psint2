from rest_framework import serializers
from .models import *
from .views import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    Pets = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='pet-detail')

    class Meta:
        model = User
        fields = ['Name', 'Surname', 'Login', 'Password', 'Mail', 'Pets']


class PetSerializer(serializers.HyperlinkedModelSerializer):
    Pet_User = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='Surname')
    Operations = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='operation-detail')
    Visited = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='visits-detail')

    class Meta:
        model = Pet
        fields = ['Name', 'Breed', 'Pet_User', 'Operations', 'Visited']

class OperationSerializer(serializers.HyperlinkedModelSerializer):
    Operation_Pet = serializers.SlugRelatedField(queryset=Pet.objects.all(), slug_field='Name')
    Doctors = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='doctor-detail')

    class Meta:
        model = Operation
        fields = ['Name', 'Date', 'Operation_Pet', 'Doctors']


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    Doctor_Operation = serializers.SlugRelatedField(queryset=Operation.objects.all(), slug_field='Name')
    Visit = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='visits-detail')
    Receptions = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='reception-detail')

    class Meta:
        model = Doctor
        fields = ['Name', 'Surname', 'Specialization', 'Doctor_Operation', 'Visit','Receptions']


class VisitsSerializers(serializers.ModelSerializer):
    Pet_Visits = serializers.SlugRelatedField(queryset=Pet.objects.all(), slug_field='Name')
    Doctor_Visits = serializers.SlugRelatedField(queryset=Doctor.objects.all(), slug_field='Surname')

    class Meta:
        model = Visits
        fields = ['Date', 'Pet_Visits', 'Doctor_Visits']

class ReceptionSerializers(serializers.ModelSerializer):
    Doctor_Reception = serializers.SlugRelatedField(queryset=Doctor.objects.all(), slug_field='Surname')


    class Meta:
        model = Reception
        fields = ['Name_Reception', 'Descriptions', 'Doctor_Reception']

