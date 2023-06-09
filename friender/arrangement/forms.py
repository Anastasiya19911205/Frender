from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from .models import *

def validate_length_description(value):
    if len(value.split())<3:
        raise ValidationError(
            "need more than 2 words",

        )
def validate_length_comment_description(value):
    if len(value.split())>100:
        raise ValidationError(
            "Comment length must not exceed 100 symbols",

        )
#через ModelForm идет привязка к определенной модели
class RatingUserForm(forms.ModelForm):
    class Meta:
        model = UserRating
        exclude = ("user",)
        # widgets = {
        #     "description": forms.Textarea(attrs={"cols":80, "rows":20})
        # }


# class RatingUserForm(forms.Form):
#     rating = forms.IntegerField(validators=[
#         MaxValueValidator(5, message='input rating between 1 and 5'),
#         MinValueValidator(1, message='input rating between 1 and 5')
#
#     ])
#     description = forms.CharField(
#         validators=[
#             MinLengthValidator(1, message='input more than 1 symbol'),
#             validate_length_description
#         ],
#         widget=forms.Textarea(
#             attrs={
#                 'cols':30,
#                 'rows':3,
#                 'placeholder':'you opinion about arrangement',
#                 'class':'special'
#             }
#         )
#     )

class EstablishmentCreateForm(forms.ModelForm):
    class Meta:
        model = Establishments
        fields = ("name","category","address","phone")

class ArrangementForm(forms.Form):
    host = forms.ChoiceField(choices=Host.objects.values_list('id','name'))  #вывести всех наших пользователей в choices формате, values_list- позволяет вывести список данных
    place = forms.ChoiceField(choices=Establishments.objects.values_list('id','name'))

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('email',)


class BookingUserForm(forms.ModelForm):
    class Meta:
        model = Arrangements
        fields = ['host', 'guest', 'establishments']

class CommentEstUserForm(forms.Form):
        name = forms.CharField()


        description = forms.CharField(validators=[
            MinLengthValidator(1, message='input more than 1 symbol'),
            validate_length_comment_description
        ])
        rating = forms.IntegerField(validators=[
            MaxValueValidator(5, message='input rating between 1 and 5'),
            MinValueValidator(1, message='input rating between 1 and 5')

        ])





