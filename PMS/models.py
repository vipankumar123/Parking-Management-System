from django.db import models
from account.models import User

# Create your models here.


class Building(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,)
    building_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    total_floors = models.PositiveIntegerField(default=2)
    total_rows = models.PositiveIntegerField(default=10)
    total_coloumn = models.PositiveIntegerField()
    

class Floor(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_name = models.CharField(max_length=40)

class Rows(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE,)
    Row_name = models.CharField(max_length=50)



