# Generated by Django 2.1.2 on 2018-11-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20181125_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(),
        ),
    ]
