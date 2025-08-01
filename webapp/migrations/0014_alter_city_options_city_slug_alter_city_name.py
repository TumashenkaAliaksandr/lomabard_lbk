# Generated by Django 5.2.3 on 2025-07-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_address_city_delete_location_address_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Город'),
        ),
    ]
