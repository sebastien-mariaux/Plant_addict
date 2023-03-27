from django.urls import reverse
from django.views.generic import ListView, UpdateView
from encyclopedia.models import Specie
from encyclopedia.forms import SpecieForm


class SpecieListView(ListView):
    model = Specie
    template_name = 'species_list.html'
    paginate_by = 15
    context_object_name = 'species'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('genus', 'genus__family')
        search_specie = self.request.GET.get('search_specie')
        search_genus = self.request.GET.get('search_genus')
        search_family = self.request.GET.get('search_family')
        if search_specie:
            queryset = queryset.filter(name__startswith=search_specie)
        if search_genus:
            queryset = queryset.filter(genus__name__startswith=search_genus)
        if search_family:
            queryset = queryset.filter(genus__family__name__startswith=search_family)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_specie'] = self.request.GET.get('search_specie') or ''
        context['search_genus'] = self.request.GET.get('search_genus') or ''
        context['search_family'] = self.request.GET.get('search_family') or ''
        return context


class SpecieUpdateView(UpdateView):
    model = Specie

    form_class = SpecieForm

    def get_success_url(self):
        return reverse('species_list')


