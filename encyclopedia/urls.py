
from django.urls import path
from django.views.generic import TemplateView
from encyclopedia.views.species_views import SpeciesList


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('species/', SpeciesList.as_view(), name='species_list'),
]
