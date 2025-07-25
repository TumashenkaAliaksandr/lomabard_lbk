# Generated by Django 5.2.3 on 2025-07-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_product_flags_product_is_children_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(verbose_name='Год')),
                ('balance_pdf', models.FileField(upload_to='financials/', verbose_name='Бухгалтерский баланс (PDF)')),
                ('notes_pdf', models.FileField(upload_to='financials/', verbose_name='Примечания к балансу (PDF)')),
                ('profit_loss_pdf', models.FileField(upload_to='financials/', verbose_name='Отчет о прибылях и убытках (PDF)')),
                ('capital_change_pdf', models.FileField(upload_to='financials/', verbose_name='Отчет об изменении капитала (PDF)')),
                ('cash_flow_pdf', models.FileField(upload_to='financials/', verbose_name='Отчет о движении денежных средств (PDF)')),
            ],
            options={
                'verbose_name': 'Финансовая отчетность',
                'verbose_name_plural': 'Финансовые отчетности',
            },
        ),
    ]
