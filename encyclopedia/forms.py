from django import forms
from django.forms import ModelForm
from encyclopedia.models import Specie, Genus


class SpecieForm(ModelForm):
    class Meta:
        model = Specie
        fields = ['name', 'genus', 'cover_picture']

    genus = forms.HiddenInput()


class GenusForm(ModelForm):
    class Meta:
        model = Genus
        fields = ['name', 'family', 'cover_picture']

    family = forms.HiddenInput()
