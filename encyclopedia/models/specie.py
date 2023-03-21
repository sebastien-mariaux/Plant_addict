"""
Data source : http://www.worldfloraonline.org/downloadData
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from plant_addict.models import DatedModel


class Specie(DatedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('scientific name'),
        null=False, blank=False,
        unique=True,
    )
    source_id = models.CharField(
        max_length=15,
        verbose_name=_('source id'),
        null=False, blank=False,
    )
    source_reference = models.CharField(
        max_length=255,
        verbose_name=_('source reference'),
        null=True, blank=True,
    )
    genus = models.ForeignKey(
        'Genus',
        on_delete=models.CASCADE,
        verbose_name=_('genus'),
        null=False, blank=False,
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('specie')
        verbose_name_plural = _('species')
        ordering = ['name']
        app_label = 'encyclopedia'
