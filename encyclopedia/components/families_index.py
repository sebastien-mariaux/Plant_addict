
from encyclopedia.components.unicorn_index import UnicornIndexView
from encyclopedia.models import Genus


class FamiliesIndexView(UnicornIndexView):
    family_name = ''

    def get_queryset(self):
        queryset = Genus.objects.all()
        if self.family_name:
            queryset = queryset.filter(family__name__startswith=self.family_name)
        return queryset

    def reset(self):
        self.family_name = ''
        super().reset()
