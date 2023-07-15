# Generated by Django 4.2.2 on 2023-06-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship_params',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('distance', models.FloatField()),
                ('weight', models.FloatField()),
                ('price', models.FloatField()),
                ('extracost', models.FloatField()),
                ('volume_item', models.FloatField()),
                ('volume_journey', models.FloatField()),
                ('volume_origin_center', models.FloatField()),
                ('carrier', models.FloatField()),
            ],
        ),
    ]
