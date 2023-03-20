from django.db import models
from django.utils.translation import gettext_lazy as _
from plant_addict.models import DatedModel


class PlantClass(DatedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
        null=False, blank=False,
        unique=True,
    )

    branch = models.ForeignKey(
        'Branch',
        on_delete=models.CASCADE,
        verbose_name=_('branch'),
        null=True, blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('class')
        verbose_name_plural = _('classes')
        ordering = ['name']
        app_label = 'encyclopedia'
