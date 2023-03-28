from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from plant_addict.models import DatedModel


class Plant(DatedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        null=False, blank=False,
    )
    specie = models.ForeignKey(
        'encyclopedia.Specie',
        verbose_name=_('Specie'),
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )
    acquisition_date = models.DateField(
        verbose_name=_('Acquisition date'),
        null=True, blank=True,
    )

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = _('Plant')
        verbose_name_plural = _('Plants')
        app_label = 'collection'


class PlantPicture(DatedModel):
    plant = models.ForeignKey(
        'Plant',
        verbose_name=_('Plant'),
        on_delete=models.CASCADE,
        null=False, blank=False,
    )
    picture = models.ImageField(
        upload_to='media/images/plants/pictures',
        verbose_name=_('Picture'),
        null=False, blank=False,
    )
    cover = models.BooleanField(
        verbose_name=_('Cover picture'),
        default=True,
    )

    def __str__(self) -> str:
        return str(self.plant.name)

    class Meta:
        verbose_name = _('Plant picture')
        verbose_name_plural = _('Plant pictures')
        app_label = 'collection'
