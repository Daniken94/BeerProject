# Generated by Django 3.2.10 on 2022-01-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorApp', '0005_auto_20220104_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='fg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Gęstość końcowa BLG'),
        ),
        migrations.AddField(
            model_name='beer',
            name='og',
            field=models.IntegerField(blank=True, null=True, verbose_name='Gęstość początkowa BLG'),
        ),
    ]
