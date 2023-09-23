from django import forms
from .models import Review

class Applicantform(forms.ModelForm):
    class Meta:
        model= Review
        fields= ['Name','Mail','Enter_your_thoughts']