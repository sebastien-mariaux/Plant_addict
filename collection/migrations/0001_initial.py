# Generated by Django 4.1.7 on 2023-03-28 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encyclopedia', '0002_family_cover_picture_genus_cover_picture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='media/images/plants/cover_pictures', verbose_name='Picture')),
                ('description', models.TextField(verbose_name='Description')),
                ('acquisition_date', models.DateField(blank=True, null=True, verbose_name='Acquisition date')),
                ('specie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='encyclopedia.specie', verbose_name='Specie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]