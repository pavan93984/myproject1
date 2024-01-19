from django import forms
from jobpostapp.models import apply

class creatapply(forms.ModelForm):
    class Meta:
        model = apply
        fields = "__all__"