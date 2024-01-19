from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField
from myapp1.models import imgpro,author,comment,subscribe


class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
    captcha = ReCaptchaField()

class imgpro1(forms.ModelForm):
    class Meta:
        model = imgpro
        fields = ['img']

class daily_post(forms.ModelForm):
    class Meta:
        model = author
        fields = "__all__"

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['Content','Name','Email']

class subscribes(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = "__all__"


