# Generated by Django 3.2.11 on 2022-11-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0005_beer_brew'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='ebc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
