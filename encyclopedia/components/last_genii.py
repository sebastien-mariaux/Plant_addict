
from django_unicorn.components import UnicornView, QuerySetType
from encyclopedia.models import Genus


class LastGeniiView(UnicornView):
    search: str = ""
    genii:QuerySetType[Genus] = Genus.objects.all().order_by('-id')[:5]

    def hydrate(self):
        self.genii = Genus.objects.filter(name__icontains=self.search).order_by('-id')[:5]

    def reset(self):
        self.search = ""
        self.genii = Genus.objects.all().order_by('-id')[:5]