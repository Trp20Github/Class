from django import forms
from .models import *
class regform(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = regmodel
        fields = ['name', 'email', 'phone', 'password']

class logform(forms.Form):
    email = forms.CharField(max_length=80)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class studentform(forms.ModelForm):
    student_name = forms.CharField(label='Student Name', max_length=50)
    image = forms.ImageField(widget=forms.FileInput)
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput)
    email = forms.EmailField(label='Email ID', widget=forms.EmailInput, max_length=80)
    maths_score = forms.IntegerField(label='Maths Score', widget=forms.NumberInput)
    Physics_score = forms.IntegerField(label='Physics score', widget=forms.NumberInput)
    Chemistry_score = forms.IntegerField(label='Chemistry score', widget=forms.NumberInput)

    class Meta:
        model = StudentDetails
        fields = ['student_name', 'image', 'dob', 'email', 'maths_score', 'Physics_score', 'Chemistry_score']


class itemform(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Uploadimage
        fields = ['itemname', 'image']
