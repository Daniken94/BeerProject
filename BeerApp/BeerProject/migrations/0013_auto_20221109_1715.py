# Generated by Django 3.2.11 on 2022-11-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeerProject', '0012_auto_20221106_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='beer_image',
            field=models.ImageField(default='product_images/default.png', null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='unit',
            field=models.CharField(choices=[('litres', 'litres')], default='litres', max_length=50),
        ),
        migrations.AlterField(
            model_name='beerimage',
            name='image',
            field=models.ImageField(default='product_images/default.png', null=True, upload_to='product_images'),
        ),
    ]
