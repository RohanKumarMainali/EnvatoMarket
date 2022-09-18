from django import forms
from .models import *

class PackageForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id':'richtext_field'}))

    class Meta:
        model = Package
        fields="__all__" 