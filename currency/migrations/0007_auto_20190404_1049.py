# Generated by Django 2.2 on 2019-04-04 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_auto_20190404_0448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='czk_name',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='euro_name',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='pln_name',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='usd_name',
        ),
    ]
