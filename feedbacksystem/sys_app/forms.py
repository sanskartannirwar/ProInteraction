from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Feedback


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



course_ch = (("Web Designing", "Web Designing"),
             ("Full Stack Python", "Full Stack Python"),
             ("Data Science", "Data Science"),
             ("Web Development", "Web Development"))


class Contactdetails(forms.Form):
    name = forms.CharField(label="Name", max_length=30)
    email = forms.EmailField(label="Email")
    mobile_number = forms.IntegerField(label="Mobile No")
    course = forms.ChoiceField(choices=course_ch)
    address = forms.CharField(label="Address", max_length=150)



class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'feedback']
