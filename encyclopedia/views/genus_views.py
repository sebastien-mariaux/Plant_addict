from django.views.generic import ListView, View
from django.http import JsonResponse
from encyclopedia.models import Genus


class GenusListView(ListView):
    model = Genus
    template_name = 'genuses_list.html'
    paginate_by = 15
    context_object_name = 'genuses'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('family')
        search_genus = self.request.GET.get('search_genus')
        search_family = self.request.GET.get('search_family')
        if search_genus:
            queryset = queryset.filter(name__startswith=search_genus)
        if search_family:
            queryset = queryset.filter(family__name__startswith=search_family)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_genus'] = self.request.GET.get('search_genus') or ''
        context['search_family'] = self.request.GET.get('search_family') or ''
        return context


class GenusSearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        genuses = self.get_genus_data(query)
        return JsonResponse({'results': genuses})

    def get_genus_data(self, query):
        genuses = Genus.objects.filter(name__startswith=query).all()
        return list(genuses.values('pk', 'name')[0:25])
