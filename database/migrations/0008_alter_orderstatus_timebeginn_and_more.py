# Generated by Django 4.0.6 on 2022-07-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_alter_orderdata_orderdate_alter_orderdata_ordertime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='timeBeginn',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='timeEnd',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
