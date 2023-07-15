# Generated by Django 4.2.2 on 2023-06-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipparams', '0010_alter_ship_params_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship_params',
            name='time',
        ),
        migrations.RemoveField(
            model_name='ship_params',
            name='zone',
        ),
        migrations.AddField(
            model_name='ship_params',
            name='days',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='ship_params',
            name='lat1',
            field=models.FloatField(default=10.0),
        ),
        migrations.AddField(
            model_name='ship_params',
            name='lat2',
            field=models.FloatField(default=10.0),
        ),
        migrations.AddField(
            model_name='ship_params',
            name='lon1',
            field=models.FloatField(default=10.0),
        ),
        migrations.AddField(
            model_name='ship_params',
            name='lon2',
            field=models.FloatField(default=10.0),
        ),
        migrations.AddField(
            model_name='ship_params',
            name='mode',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='ship_params',
            name='slot',
            field=models.FloatField(default=1),
        ),
    ]
