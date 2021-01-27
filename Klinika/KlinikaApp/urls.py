from django.urls import path
from . import views

urlpatterns = [

   path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

   path('User/', views.UserList.as_view(), name=views.UserList.name),
   path('User/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

   path('Pet', views.PetList.as_view(), name=views.PetList.name),
   path('Pet/<int:pk>', views.PetDetail.as_view(), name=views.PetDetail.name),

   path('Operation/', views.OperationList.as_view(), name=views.OperationList.name),
   path('Operation/<int:pk>', views.OperationDetail.as_view(), name=views.OperationDetail.name),

   path('Doctor', views.DoctorList.as_view(), name=views.DoctorList.name),
   path('Doctor/<int:pk>', views.DoctorDetail.as_view(), name=views.DoctorDetail.name),

   path('Visits', views.VisitsList.as_view(), name=views.VisitsList.name),
   path('Visits/<int:pk>', views.VisitsDetail.as_view(), name=views.VisitsDetail.name),

   path('Reception', views.ReceptionList.as_view(), name=views.ReceptionList.name),
   path('Reception/<int:pk>', views.ReceptionDetail.as_view(), name=views.ReceptionDetail.name),

]