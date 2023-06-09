# Generated by Django 4.1.7 on 2023-03-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='cover_picture',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='media/images/families/cover_pictures',
                verbose_name='cover picture'),
        ),
        migrations.AddField(
            model_name='genus',
            name='cover_picture',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='media/images/genuses/cover_pictures',
                verbose_name='cover picture'),
        ),
        migrations.AddField(
            model_name='specie',
            name='cover_picture',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='media/images/species/cover_pictures',
                verbose_name='cover picture'),
        ),
    ]
