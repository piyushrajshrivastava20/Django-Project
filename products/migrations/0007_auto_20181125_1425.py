# Generated by Django 2.1.2 on 2018-11-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181125_1424'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]
