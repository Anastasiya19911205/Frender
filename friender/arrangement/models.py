from django.db import models
from django.db.models import F
from datetime import datetime
from django.core.signals import request_finished
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver

STATUS = [
    ('a','available'),
    ('b','busy')
]

SEX = [
    ('m', 'male'),
    ('f', 'female')
]
CATEGORY =[
    ('c', 'cafe'),
    ('r', 'restaurant'),
    ('p', 'pub')
]
HOBBIES =[
    ('sp', 'sport'),
    ('tr', 'traveling'),
    ('pt', 'painting'),
    ('cg', 'computer_games'),
    ('sh', 'shopping'),
    ('ph', 'photo'),
    ('ms', 'music'),
]
class Users(models.Model):
    name = models.CharField(max_length=100,verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст')
    sex = models.CharField(max_length=1, choices=SEX,verbose_name='пол')
    email = models.EmailField(null=True, verbose_name='почта')
    city = models.CharField(max_length=100, default='Minsk', verbose_name='город')
    photo = models.ImageField(upload_to="photo_user", null=True)
    class Meta:
    #     indexes = [
    #         models.Index(fields=["age", 'name']),
    #         models.Index(fields=['name']),
    #         models.Index(fields=['-name']),
    #         models.Index(fields=["age"]),
    #         models.Index(fields=['-age']),
    #         models.Index(fields=['name', '-sex']),
    #         models.Index(fields=['age', 'sex']),
    # ]
        verbose_name = 'пользователи'
        verbose_name_plural = 'пользователи'
    def __str__(self):
        return self.name

class Host(Users):
    max_spend_value = models.PositiveIntegerField(null=True)
    status = models.CharField(choices=STATUS, max_length=1, default='a')

    def __str__(self):
        return f"{self.name} ({self.max_spend_value})"

    # class Meta:
    #     verbose_name_plural = 'приглашающие'

class Guest(Users):
    min_bill_value = models.PositiveIntegerField(null=True)
    def __str__(self):
        return f"{self.name} ({self.min_bill_value})"

    # class Meta:
    #     verbose_name_plural = 'гости'
class Passport(models.Model):
    passport_id = models.CharField(max_length=10, unique=True)
    date_create = models.DateTimeField(auto_now=datetime.utcnow())
    user = models.OneToOneField('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_id

class Hobbies(models.Model):
    hobby = models.CharField(max_length=100,verbose_name= "хобби")
    category = models.CharField(max_length=2, choices=HOBBIES, verbose_name='категория')
    user = models.ManyToManyField("Users")

    def __str__(self):
        return str(self.hobby)


    class Meta:
        verbose_name_plural = 'хобби'
class Arrangements(models.Model):
    host = models.ForeignKey('Host', on_delete=models.CASCADE, null=True, verbose_name='приглашающий')
    guest = models.ForeignKey('Guest', on_delete=models.CASCADE, null=True, verbose_name='гость')
    establishments = models.ForeignKey('Establishments', on_delete=models.CASCADE, verbose_name='заведение')



class Establishments(models.Model):
    name = models.CharField(max_length=15, verbose_name='наименование')
    category = models.CharField(max_length=1, choices=CATEGORY, verbose_name='категория')
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    photo = models.ImageField(upload_to="photo_establishments", null=True)
    def __str__(self):
        return f"{self.name}"

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category'])
        ]
        verbose_name_plural = 'заведения'
class Rating(models.Model):
    rating = models.PositiveIntegerField()
    description = models.CharField(max_length=255)


    class Meta:
        abstract = True

class EstablishmentsRating(Rating):
    establishment = models.ForeignKey('Establishments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.establishment)

class UserRating(Rating):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photo_ratings",null=True) # "upload_to"- наименование папки куда загружаем фото
    def __str__(self):
        return str(self.rating)

# @receiver(post_save, sender=Users)
def user_created(sender, instance, **kwargs):
    print('signal work')
    print(sender)
    print(instance)
    print(instance.age)
    hobby = Hobbies.objects.get(id=1)
    instance.hobbies_set.add(hobby)

#
post_save.connect(receiver=user_created, sender=Users)

# class Establishmensts(models.Model):
#     name_place = models.CharField(max_length=40)
#     category_place = models.CharField(max_length=1, choices=CATEGORY)
#     address_place = models.CharField(max_length=40)
#     phone = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name_place

# def user_created(sender, instance, **kwargs):
#     print('signal work')
#     print(sender)
#     print(instance)
#     print(instance.age)
#
#     hobby = Hobbies.objects.get(id=1)
#     instance.hobbies_set.add(hobby)
#
# post_save.connect(receiver=user_created, sender=Users)