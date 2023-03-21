
from encyclopedia.components.unicorn_index import UnicornIndexView
from encyclopedia.models import Genus


class FamiliesIndexView(UnicornIndexView):
    family_name = ''

    def get_queryset(self):
        qs = Genus.objects.all()
        if self.family_name:
            qs = qs.filter(family__name__startswith=self.family_name)
        return qs

    def reset(self):
        self.genus_name = ''
        self.family_name = ''
        super().reset()
