# Generated by Django 3.2.11 on 2022-12-27 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0019_alter_ingredients_aac'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='bootled_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='bootled at'),
            preserve_default=False,
        ),
    ]
