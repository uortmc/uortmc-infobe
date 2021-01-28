# Generated by Django 3.1.5 on 2021-01-27 23:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('infobackendapp', '0008_auto_20210127_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100, verbose_name='Message')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation Date')),
                ('ascDoctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infobackendapp.doctor')),
            ],
        ),
    ]
