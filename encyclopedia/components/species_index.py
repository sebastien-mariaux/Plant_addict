from encyclopedia.models import Specie
from encyclopedia.components.unicorn_index import UnicornIndexView

class SpeciesIndexView(UnicornIndexView):
    specie_name = ''
    genus_name = ''
    family_name = ''

    def get_queryset(self):
        qs = Specie.objects.all()
        if self.specie_name:
            qs = qs.filter(name__startswith=self.specie_name)
        if  self.genus_name:
            qs = qs.filter(genus__name__startswith=self.genus_name)
        if self.family_name:
            qs = qs.filter(genus__family__name__startswith=self.family_name)
        return qs

    def reset(self):
        self.specie_name = ''
        self.genus_name = ''
        self.family_name = ''
        super().reset()

