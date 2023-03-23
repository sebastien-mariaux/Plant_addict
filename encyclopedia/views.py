from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import UpdateView, View
from encyclopedia.models import Specie, Genus
from encyclopedia.forms import SpecieForm


class EditSpecieView(UpdateView):
    model = Specie

    form_class = SpecieForm

    def get_success_url(self):
        return reverse('species_list')


class GenusSearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        genuses = self.get_genus_data(query)
        return JsonResponse({'results': genuses})

    def get_genus_data(self, query):
        genuses = Genus.objects.filter(name__startswith=query).all()
        return list(genuses.values('pk', 'name')[0:25])
