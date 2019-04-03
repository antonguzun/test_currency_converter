# Generated by Django 2.2 on 2019-04-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_auto_20190402_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_cost', models.FloatField()),
                ('euro_cost', models.FloatField()),
                ('czk_cost', models.FloatField()),
                ('pln_cost', models.FloatField()),
                ('pub_date', models.DateField(verbose_name='last update')),
            ],
        ),
        migrations.RemoveField(
            model_name='currency_euro',
            name='usd',
        ),
        migrations.RemoveField(
            model_name='currency_pln',
            name='usd',
        ),
        migrations.DeleteModel(
            name='currency_Czk',
        ),
        migrations.DeleteModel(
            name='currency_Euro',
        ),
        migrations.DeleteModel(
            name='currency_Pln',
        ),
        migrations.DeleteModel(
            name='currency_USD',
        ),
    ]