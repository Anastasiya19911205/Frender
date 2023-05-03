from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from .models import *

def validate_length_description(value):
    if len(value.split())<3:
        raise ValidationError(
            "need more than 2 words",

        )



class RatingUserForm(forms.Form):
    rating = forms.IntegerField(validators=[
        MaxValueValidator(5, message='input rating between 1 and 5'),
        MinValueValidator(1, message='input rating between 1 and 5')

    ])
    description = forms.CharField(
        validators =[
            MinLengthValidator(1, message='input more than 1 symbol'),
            validate_length_description
        ],
        widget=forms.Textarea(
            attrs={
                'cols':30,
                'rows':3,
                'placeholder':'you opinion about arrangement',
                'class':'special'
            }
        )
    )
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('email',)
        age = forms.IntegerField(validators=[
            MaxValueValidator(90, message='enter your age from 18 to 90 years old'),
            MinValueValidator(18, message='enter your age from 18 to 90 years old')

        ])


class BookingUserForm(forms.ModelForm):
    class Meta:
        model = Arrangements
        fields = ['host', 'guest', 'establishments']

class CommentEstUserForm(forms.Form):
        name = forms.CharField()


        description = forms.CharField(validators=[
            MinLengthValidator(1, message='input more than 1 symbol'),
            validate_length_description
        ])


