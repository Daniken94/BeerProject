# Generated by Django 3.2.10 on 2022-01-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalculatorApp', '0011_ingredients_sequence'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='sequence_unit',
            field=models.CharField(default=10, max_length=120),
            preserve_default=False,
        ),
    ]
