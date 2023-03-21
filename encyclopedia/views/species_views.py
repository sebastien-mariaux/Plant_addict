from django.views.generic import TemplateView
from encyclopedia.models import Specie

class SpeciesList(TemplateView):
    # paginate_by = 20
    # model = Specie
    template_name = 'species_list.html'
    # context_object_name = 'species'

    # def get_context_data(self, **kwargs):
    #     context = super(SpeciesList, self).get_context_data(**kwargs)
    #     context['species_list'] = Specie.objects.all()
    #     return context