# Generated by Django 2.1.2 on 2018-11-27 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_delete_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('ame', models.CharField(max_length=10)),
                ('played', models.CharField(max_length=10)),
                ('namewins', models.CharField(max_length=10)),
                ('amewins', models.CharField(max_length=10)),
                ('tie', models.CharField(max_length=10)),
            ],
        ),
    ]
