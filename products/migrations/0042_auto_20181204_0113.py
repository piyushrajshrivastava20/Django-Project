# Generated by Django 2.1.2 on 2018-12-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_ground_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ground',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
