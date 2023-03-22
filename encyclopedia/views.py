from django.views.generic import UpdateView
from encyclopedia.models import Specie


class EditSpecieView(UpdateView):
    model = Specie
    fields = ['name', 'genus']