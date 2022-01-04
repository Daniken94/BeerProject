# Generated by Django 3.2.10 on 2022-01-03 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('tagline', models.CharField(max_length=120, verbose_name='Beer style')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('abv', models.FloatField(blank=True, null=True)),
                ('ibu', models.IntegerField(blank=True, null=True)),
                ('ebc', models.IntegerField(blank=True, null=True)),
                ('ph', models.IntegerField(blank=True, null=True)),
                ('attenuation_level', models.FloatField(blank=True, null=True)),
                ('beer_value', models.IntegerField()),
                ('unit', models.IntegerField(choices=[(1, 'litres')])),
            ],
        ),
        migrations.CreateModel(
            name='BeerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Fermentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_temperature', models.IntegerField()),
                ('unit', models.IntegerField(choices=[(1, 'celsius')])),
                ('duration', models.IntegerField(blank=True, help_text='How long in days', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('type', models.IntegerField(choices=[(1, 'malt'), (2, 'hops'), (3, 'yeast'), (4, 'other')])),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('value', models.FloatField()),
                ('unit', models.IntegerField(choices=[(1, 'litres'), (2, 'kilograms'), (3, 'grams')])),
                ('ebc', models.IntegerField(blank=True, null=True)),
                ('purpose', models.IntegerField(blank=True, choices=[(1, 'bittering'), (2, 'aroma'), (3, 'dual use'), (4, 'malt')], null=True)),
                ('aac', models.IntegerField(blank=True, null=True, verbose_name='Alfa acid')),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.CreateModel(
            name='MashTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_temperature', models.IntegerField()),
                ('unit', models.IntegerField(choices=[(1, 'celsius')])),
                ('duration', models.IntegerField(help_text='How long in minutes')),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fermentation', models.ManyToManyField(to='CalculatorApp.Fermentation')),
                ('mash_temp', models.ManyToManyField(to='CalculatorApp.MashTemp')),
            ],
        ),
        migrations.CreateModel(
            name='BoilVolume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('unit', models.IntegerField(choices=[(1, 'litres')])),
                ('substance', models.CharField(max_length=120)),
                ('beer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='CalculatorApp.beer')),
            ],
        ),
        migrations.CreateModel(
            name='BeerProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='last updated')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CalculatorApp.beer', verbose_name='Choose beer')),
                ('beer_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CalculatorApp.beerimage', verbose_name='Choose image')),
                ('boil_volume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CalculatorApp.boilvolume')),
                ('ingredients', models.ManyToManyField(to='CalculatorApp.Ingredients', verbose_name='Ingredients')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CalculatorApp.method', verbose_name='Choose mash method')),
            ],
        ),
    ]