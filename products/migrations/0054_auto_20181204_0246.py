# Generated by Django 2.1.2 on 2018-12-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0053_auto_20181204_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='abcbat',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stats',
            name='bcdbatt',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]