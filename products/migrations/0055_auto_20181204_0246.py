# Generated by Django 2.1.2 on 2018-12-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0054_auto_20181204_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='abcbowl',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stats',
            name='bcdbowll',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
