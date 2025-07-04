# Generated by Django 5.2.3 on 2025-07-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('icon', models.ImageField(upload_to='service_icons/', verbose_name='Иконка услуги')),
                ('link', models.URLField(blank=True, verbose_name='Ссылка на страницу услуги')),
            ],
            options={
                'verbose_name': 'Иконка услуги',
                'verbose_name_plural': 'Иконки услуг',
            },
        ),
    ]
