from django_unicorn.components import UnicornView, QuerySetType
from encyclopedia.models import Specie


class LastSpeciesView(UnicornView):
    search: str = ""
    species: QuerySetType[Specie] = Specie.objects.all().order_by('-id')[:5]
    species_count: int = Specie.objects.all().count()

    def hydrate(self):
        self.species = Specie.objects.filter(name__icontains=self.search).order_by('-id')[:5]

    def reset(self):
        self.search = ""
        self.species = Specie.objects.all().order_by('-id')[:5]
