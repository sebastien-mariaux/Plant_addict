
from django_unicorn.components import UnicornView, QuerySetType
from encyclopedia.models import Genus


class LastGenusesView(UnicornView):
    search: str = ""
    genuses: QuerySetType[Genus] = Genus.objects.all().order_by('-id')[:5]
    genuses_count: int = Genus.objects.all().count()

    def hydrate(self):
        self.genuses = Genus.objects.filter(name__icontains=self.search).order_by('-id')[:5]

    def reset(self):
        self.search = ""
        self.genuses = Genus.objects.all().order_by('-id')[:5]
