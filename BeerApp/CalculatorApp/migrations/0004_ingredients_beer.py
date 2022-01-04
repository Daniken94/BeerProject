# Generated by Django 3.2.10 on 2022-01-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorApp', '0003_rename_beer_value_beer_beer_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='beer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='CalculatorApp.beer'),
            preserve_default=False,
        ),
    ]
