from urllib.parse import urlencode
from django.urls import reverse
from django.views.generic import ListView, View, CreateView, UpdateView
from django.http import JsonResponse
from encyclopedia.models import Family


class FamilyListView(ListView):
    model = Family
    template_name = 'families_list.html'
    paginate_by = 15
    context_object_name = 'families'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_family = self.request.GET.get('search_family')
        if search_family:
            queryset = queryset.filter(name__startswith=search_family)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_family'] = self.request.GET.get('search_family') or ''
        return context

class FamilySearchView(View):
    def get(self, request):
        query = request.GET.get('query')
        families = self.get_genus_data(query)
        return JsonResponse({'results': families})

    def get_genus_data(self, query):
        families = Family.objects.filter(name__startswith=query).all()
        return list(families.values('pk', 'name')[0:25])


class FamilyCreateView(CreateView):
    model = Family
    fields = ['name',  'cover_picture']

    def get_success_url(self):
        return reverse('families_list') + '?' + urlencode({'search_family': self.object.name})

class FamilyUpdateView(UpdateView):
    model = Family
    fields = ['name',  'cover_picture']

    def get_success_url(self):
        return reverse('families_list') + '?' + urlencode({'search_family': self.object.name})
