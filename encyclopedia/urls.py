
from django.urls import path
from django.views.generic import TemplateView
from encyclopedia.views import EditSpecieView, SpecieListView, GenusSearchView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('species/', SpecieListView.as_view(), name='species_list'),
    path('species/<int:pk>/edit', EditSpecieView.as_view(), name='edit_specie'),
    path('genuses/', TemplateView.as_view(template_name='genii_list.html'), name='genii_list'),
    path('genuses/search', GenusSearchView.as_view(), name='genus_search'),
    path('families/',
         TemplateView.as_view(template_name='families_list.html'),
         name='families_list'
         ),
]
