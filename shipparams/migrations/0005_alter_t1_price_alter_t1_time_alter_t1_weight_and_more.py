# Generated by Django 4.2.2 on 2023-06-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipparams', '0004_alter_t1_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t1',
            name='Price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='t1',
            name='Time',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='t1',
            name='Weight',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='t1',
            name='Zones',
            field=models.TextField(),
        ),
    ]