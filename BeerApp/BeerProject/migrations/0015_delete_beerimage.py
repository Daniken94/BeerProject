# Generated by Django 3.2.11 on 2022-11-09 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0014_remove_beer_abv'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BeerImage',
        ),
    ]