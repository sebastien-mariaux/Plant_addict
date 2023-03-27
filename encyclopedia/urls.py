
from django.urls import path
from django.views.generic import TemplateView
from encyclopedia.views.family_views import FamilyListView
from encyclopedia.views.genus_views import GenusListView, GenusSearchView
from encyclopedia.views.specie_view import SpecieListView, SpecieUpdateView, SpecieDetailView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('species/', SpecieListView.as_view(), name='species_list'),
    path('species/<int:pk>/edit', SpecieUpdateView.as_view(), name='edit_specie'),
    path('species/<int:pk>', SpecieDetailView.as_view(), name='specie_detail'),
    path('genuses/', GenusListView.as_view(), name='genuses_list'),
    path('genuses/search', GenusSearchView.as_view(), name='genus_search'),
    path('families/', FamilyListView.as_view(), name='families_list'),
]
