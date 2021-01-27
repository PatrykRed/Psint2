from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=45)
    Surname = models.CharField(max_length=45)
    Login = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
    Mail = models.CharField(max_length=45)

    def __str__(self):
        return self.Name + ' ' + self.Surname

class Pet(models.Model):
    Name = models.CharField(max_length=45)
    Breed = models.CharField(max_length=45)
    Pet_User = models.ForeignKey(User, on_delete=models.CASCADE, null=False,related_name='Pets')

    def __str__(self):
        return self.Name + ' ' + self.Breed

class Operation(models.Model):
    Name = models.CharField(max_length=45)
    Date = models.DateField(null=False)
    Operation_Pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False,related_name='Operations')

    def __str__(self):
        return self.Name


class Doctor(models.Model):
    Name = models.CharField(max_length=45)
    Surname = models.CharField(max_length=45)
    Specialization = models.CharField(max_length=45)
    Doctor_Operation = models.ForeignKey(Operation, on_delete=models.CASCADE,null=False,related_name='Doctors')

    def __str__(self):
        return self.Name + ' ' + self.Surname + ' ' + self.Specialization

class Visits(models.Model):
    Date = models.DateField(null=False)
    Pet_Visits = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False, related_name='Visited')
    Doctor_Visits = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False, related_name='Visit')

class Reception(models.Model):
    Name_Reception = models.CharField(max_length=45)
    Descriptions = models.CharField(max_length=45)
    Doctor_Reception = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=False, related_name='Receptions')



