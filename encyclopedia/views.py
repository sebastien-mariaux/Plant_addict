from django.urls import reverse
from django.views.generic import UpdateView
from encyclopedia.models import Specie


class EditSpecieView(UpdateView):
    model = Specie
    fields = ['name', 'genus', 'cover_picture']

    def get_success_url(self):
        return reverse('species_list')
