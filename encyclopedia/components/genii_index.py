from encyclopedia.components.unicorn_index import UnicornIndexView
from encyclopedia.models import Genus


class GeniiIndexView(UnicornIndexView):
    genus_name = ''
    family_name = ''

    def get_queryset(self):
        queryset = Genus.objects.all()
        if self.genus_name:
            queryset = queryset.filter(name__startswith=self.genus_name)
        if self.family_name:
            queryset = queryset.filter(family__name__startswith=self.family_name)
        return queryset

    def reset(self):
        self.genus_name = ''
        self.family_name = ''
        super().reset()
