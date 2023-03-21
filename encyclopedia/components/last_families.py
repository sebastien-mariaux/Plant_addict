
from django_unicorn.components import UnicornView, QuerySetType
from encyclopedia.models import Family


class LastFamiliesView(UnicornView):
    search: str = ""
    families: QuerySetType[Family] = Family.objects.all().order_by('-id')[:5]
    families_count: int = Family.objects.all().count()

    def hydrate(self):
        self.families = Family.objects.filter(name__icontains=self.search).order_by('-id')[:5]

    def reset(self):
        self.search = ""
        self.families = Family.objects.all().order_by('-id')[:5]
