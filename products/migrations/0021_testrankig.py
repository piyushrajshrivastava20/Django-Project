# Generated by Django 2.1.2 on 2018-11-26 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_rankig'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testrankig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odiposition', models.CharField(max_length=20)),
                ('odirating', models.CharField(max_length=20)),
                ('name', models.ForeignKey(blank=True, db_column='name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.Teams')),
            ],
        ),
    ]