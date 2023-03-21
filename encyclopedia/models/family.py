from django.db import models
from django.utils.translation import gettext_lazy as _
from plant_addict.models import DatedModel


class Family(DatedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
        null=False, blank=False,
        unique=True,
    )

    plant_order = models.ForeignKey(
        'PlantOrder',
        on_delete=models.CASCADE,
        verbose_name=_('order'),
        null=True, blank=True,
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = _('family')
        verbose_name_plural = _('families')
        ordering = ['name']
        app_label = 'encyclopedia'
