# Generated by Django 3.1.5 on 2021-01-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infobackendapp', '0006_auto_20210126_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='comments',
            field=models.TextField(default='Not Set', max_length=200, verbose_name='Comments'),
        ),
    ]