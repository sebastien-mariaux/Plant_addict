from django.views.generic import ListView
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