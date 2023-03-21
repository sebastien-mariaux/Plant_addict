from django.db import models
from django.utils.translation import gettext_lazy as _
from plant_addict.models import DatedModel


class PlantOrder(DatedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
        null=False, blank=False,
        unique=True,
    )

    plant_class = models.ForeignKey(
        'PlantClass',
        on_delete=models.CASCADE,
        verbose_name=_('class'),
        null=False, blank=False,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ['name']
        app_label = 'encyclopedia'
