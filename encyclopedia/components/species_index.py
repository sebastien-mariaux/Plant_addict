from django.core.paginator import Paginator
from django_unicorn.components import UnicornView
from encyclopedia.models import Specie


class SpeciesIndexView(UnicornView):
    specie_name = ''
    genus_name = ''
    family_name = ''
    genus = ''
    species = Specie.objects.none()
    items_per_page = 15
    page_index = 1
    # paginator = None
    # page_range = None
    page = {}

    class Meta:
        javascript_exclude = (
            "items_per_page",
        )

    def hydrate(self):
        self.set_species_list()

    def mount(self):
        self.set_species_list()

    def set_species_list(self):
        qs = self.get_queryset()
        if qs.count() == 0:
            self.species = []
            return
        paginator = Paginator(qs, self.items_per_page)
        page = paginator.page(self.page_index)
        self.page = self.serialize_page(page)
        self.species = page.object_list

    def get_queryset(self):
        qs = Specie.objects.all()
        if self.specie_name:
            qs = qs.filter(name__startswith=self.specie_name)
        if  self.genus_name:
            qs = qs.filter(genus__name__startswith=self.genus_name)
        if self.family_name:
            qs = qs.filter(genus__family__name__startswith=self.family_name)
        return qs


    def go_to_page(self, page):
        self.page_index = page
        self.set_species_list()

    def reset(self):
        self.specie_name = ''
        self.genus_name = ''
        self.family_name = ''
        self.page_index = 1
        self.set_species_list()

    def serialize_page(self, page):
        return {
            'next_page_number': page.next_page_number() if page.has_next() else None,
            'previous_page_number': page.previous_page_number() if page.has_previous() else None,
            'has_next': page.has_next(),
            'has_previous': page.has_previous(),
            'number': page.number,
            'num_pages': page.paginator.num_pages,
        }