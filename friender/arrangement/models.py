from django.db import models

# Create your models here.
SEX = [
    ('m', 'male'),
    ('f', 'female')
]

class Users(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    email = models.EmailField(null=True, unique=True)
    city = models.CharField(max_length=100, default='Minsk')

    def __str__(self):
        return self.name

class Establishmensts(models.Model):
    name_place = models.CharField(max_length=40)
    category_place = models.IntegerField()
    address_place = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
