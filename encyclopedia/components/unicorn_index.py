from django.core.paginator import Paginator
from django.db.models import QuerySet
from django_unicorn.components import UnicornView


class UnicornIndexView(UnicornView):
    items_per_page = 15
    page_index = 1
    page: dict = {}
    items: QuerySet = []

    def hydrate(self):
        self.set_items_list()

    def mount(self):
        self.set_items_list()

    def set_items_list(self):
        queryset = self.get_queryset()
        if queryset.count() == 0:
            self.items = []
            return
        paginator = Paginator(queryset, self.items_per_page)
        page = paginator.page(self.page_index)
        self.page = self.serialize_page(page)
        self.items = page.object_list

    def go_to_page(self, page):
        self.page_index = page
        self.set_items_list()

    def reset(self):
        self.page_index = 1
        self.set_items_list()

    def get_queryset(self):
        raise NotImplementedError

    def serialize_page(self, page):
        return {
            'next_page_number': page.next_page_number() if page.has_next() else None,
            'previous_page_number': page.previous_page_number() if page.has_previous() else None,
            'has_next': page.has_next(),
            'has_previous': page.has_previous(),
            'number': page.number,
            'num_pages': page.paginator.num_pages,
        }

    class Meta:
        javascript_exclude = (
            "items_per_page",
        )
