# Generated by Django 3.2.11 on 2022-11-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0011_beerimage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fermentation',
            name='unit',
            field=models.CharField(choices=[('celsius', 'celsius')], default='celsius', max_length=10),
        ),
        migrations.AlterField(
            model_name='mashtemp',
            name='unit',
            field=models.CharField(choices=[('celsius', 'celsius')], default='celsius', max_length=10),
        ),
    ]