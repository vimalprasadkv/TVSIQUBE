from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    userType=models.CharField(max_length=30)

# Create your models here.
class Cu_User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=150)
    mobile_number=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=50)
    regDte=models.DateField(auto_now_add=True)
    modDte=models.DateField(auto_now=True)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
class Iqube(models.Model):
    vehicle=models.CharField(max_length=50,null=True)
    stock=models.CharField(max_length=100,null=True)
    vehicle_color=models.CharField(max_length=30)
    vehicle_desc=models.CharField(max_length=200)
    rate=models.CharField(max_length=30)
    img=models.ImageField()
    status=models.CharField(max_length=30)
    regDte=models.DateField(auto_now_add=True)
class Booking(models.Model):
    date=models.DateField()
    regDte=models.DateField(auto_now_add=True)
    user=models.ForeignKey(Cu_User,on_delete=models.CASCADE)
    id_proof=models.ImageField()
    vehicles=models.ForeignKey(Iqube,on_delete=models.CASCADE)
    status=models.CharField(default="pending",max_length=50)
    


  
    
    
    
