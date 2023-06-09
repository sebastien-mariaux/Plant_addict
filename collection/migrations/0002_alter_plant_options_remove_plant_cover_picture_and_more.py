# Generated by Django 4.1.7 on 2023-03-28 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={'verbose_name': 'Plant', 'verbose_name_plural': 'Plants'},
        ),
        migrations.RemoveField(
            model_name='plant',
            name='cover_picture',
        ),
        migrations.CreateModel(
            name='PlantPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('picture', models.ImageField(upload_to='media/images/plants/pictures', verbose_name='Picture')),
                ('cover', models.BooleanField(default=True, verbose_name='Cover picture')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.plant', verbose_name='Plant')),
            ],
            options={
                'verbose_name': 'Plant picture',
                'verbose_name_plural': 'Plant pictures',
            },
        ),
    ]
