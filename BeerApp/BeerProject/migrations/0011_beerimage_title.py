# Generated by Django 3.2.11 on 2022-11-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0010_beer_alc'),
    ]

    operations = [
        migrations.AddField(
            model_name='beerimage',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
