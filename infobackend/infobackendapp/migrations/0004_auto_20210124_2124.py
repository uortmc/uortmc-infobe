# Generated by Django 3.1.5 on 2021-01-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infobackendapp', '0003_auto_20210124_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='title',
            field=models.CharField(default='Doctors Title not set', max_length=30, verbose_name='Title'),
        ),
    ]
