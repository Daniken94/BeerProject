# Generated by Django 3.2.11 on 2022-12-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0022_alter_ingredients_sequence_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='bootled_date',
            field=models.DateField(blank=True, help_text='np. 01.01.2023', null=True, verbose_name='bootled at'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='brew',
            field=models.IntegerField(help_text='Brew number'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='brew_date',
            field=models.DateField(blank=True, help_text='np. 01.01.2023', null=True, verbose_name='brewed at'),
        ),
    ]
