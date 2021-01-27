from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import permissions


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['Name','Surname']
    filterset_fields =['Name','Surname']
    ordering_fields = ['Name','Surname']
    name = 'user-list'
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated]

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    search_fields = ['Name','Breed']
    filterset_fields =['Name','Breed']
    ordering_fields = ['Name','Breed']
    name = 'pet-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    name = 'pet-detail'
    permission_classes = [permissions.IsAuthenticated]

class OperationList(generics.ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    search_fields = ['Name','Date']
    filterset_fields =['Name','Date']
    ordering_fields = ['Name','Date']
    name = 'operation-list'
    permission_classes = [permissions.IsAuthenticated]

class OperationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    name = 'operation-detail'
    permission_classes = [permissions.IsAuthenticated]

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    search_fields = ['Name','Surname','Specialization']
    filterset_fields =['Name','Surname','Specialization']
    ordering_fields = ['Name','Surname','Specialization']
    name = 'doctor-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    name = 'doctor-detail'
    permission_classes = [permissions.IsAuthenticated]

class VisitsList(generics.ListCreateAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializers
    search_fields = ['Date']
    filterset_fields =['Date']
    ordering_fields = ['Date']
    name = 'visits-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VisitsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializers
    name = 'visits-detail'
    permission_classes = [permissions.IsAuthenticated]

class ReceptionList(generics.ListCreateAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializers
    search_fields = ['Name_Reception']
    filterset_fields =['Name_Reception']
    ordering_fields = ['Name_Reception']
    name = 'reception-list'
    permission_classes = [permissions.IsAuthenticated]

class ReceptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializers
    name = 'reception-detail'
    permission_classes = [permissions.IsAuthenticated]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request):
        return Response({'User': reverse(UserList.name, request=request),
                         'Pet': reverse(PetList.name, request=request),
                         'Operation': reverse(OperationList.name, request=request),
                         'Doctor': reverse(DoctorList.name, request=request),
                         'Visits': reverse(VisitsList.name, request=request),
                         'Reception': reverse(ReceptionList.name, request=request),

                         })