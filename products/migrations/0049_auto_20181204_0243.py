# Generated by Django 2.1.2 on 2018-12-04 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0048_auto_20181204_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='ame',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stats',
            name='name',
            field=models.ForeignKey(db_column='name', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='products.Teams'),
            preserve_default=False,
        ),
    ]