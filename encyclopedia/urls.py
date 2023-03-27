
from django.urls import path
from django.views.generic import TemplateView
from encyclopedia.views import EditSpecieView, SpecieListView, GenusSearchView, GenusListView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('species/', SpecieListView.as_view(), name='species_list'),
    path('species/<int:pk>/edit', EditSpecieView.as_view(), name='edit_specie'),
    path('genuses/',GenusListView.as_view(), name='genuses_list'),
    path('genuses/search', GenusSearchView.as_view(), name='genus_search'),
    path('families/',
         TemplateView.as_view(template_name='families_list.html'),
         name='families_list'
         ),
]
