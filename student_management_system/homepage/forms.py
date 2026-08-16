from django import forms
from django.core.validators import MinLengthValidator

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class AnnouncementForm(forms.Form):
    title = forms.CharField(max_length=100, validators=[MinLengthValidator(5)])
    content = forms.CharField(max_length=500, widget=forms.Textarea, validators=[MinLengthValidator(10)])

class CourseForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[MinLengthValidator(5)])
    description = forms.CharField(max_length=500, widget=forms.Textarea, validators=[MinLengthValidator(10)])
    
