# Generated by Django 2.2 on 2019-04-02 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency_czk',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='currency_euro',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='currency_pln',
            name='pub_date',
        ),
    ]