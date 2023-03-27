from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import UpdateView, View, ListView
from encyclopedia.models import Specie, Genus, Family
from encyclopedia.forms import SpecieForm


