from django.db import models
from django.utils.translation import gettext_lazy as _
from plant_addict.models import DatedModel


class Genus(DatedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
        null=False, blank=False,
        unique=True,
    )

    family = models.ForeignKey(
        'Family',
        on_delete=models.CASCADE,
        verbose_name=_('family'),
        null=False, blank=False,
    )

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = _('genus')
        verbose_name_plural = _('genii')
        ordering = ['name']
        app_label = 'encyclopedia'
