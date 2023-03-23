from django import forms
from django.forms import ModelForm
from encyclopedia.models import Specie


class SpecieForm(ModelForm):
    class Meta:
        model = Specie
        fields = ['name', 'genus', 'cover_picture']

    genus = forms.HiddenInput()