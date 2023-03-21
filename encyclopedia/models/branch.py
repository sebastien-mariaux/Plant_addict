from django.db import models
from django.utils.translation import gettext_lazy as _
from plant_addict.models import DatedModel


class Branch(DatedModel):
    name = models.CharField(
        max_length=255,
        verbose_name=_('name'),
        null=False, blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('branch')
        verbose_name_plural = _('branches')
        ordering = ['name']
        app_label = 'encyclopedia'
