# Generated by Django 2.1.2 on 2018-11-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_abc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abcd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
            options={
                'db_table': 'Abcd',
                'managed': False,
            },
        ),
    ]
