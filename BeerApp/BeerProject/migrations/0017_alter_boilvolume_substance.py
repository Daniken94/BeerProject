# Generated by Django 3.2.11 on 2022-11-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0016_auto_20221109_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boilvolume',
            name='substance',
            field=models.CharField(default='Water', max_length=120),
        ),
    ]
