# Generated by Django 3.2.10 on 2022-01-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorApp', '0006_auto_20220104_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='fg',
            field=models.FloatField(blank=True, null=True, verbose_name='Gęstość końcowa BLG'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='og',
            field=models.FloatField(blank=True, null=True, verbose_name='Gęstość początkowa BLG'),
        ),
    ]
