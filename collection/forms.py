from django.forms import ModelForm
from collection.models import Plant


class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'specie', 'description', 'acquisition_date']
