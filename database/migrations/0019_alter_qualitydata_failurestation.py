# Generated by Django 4.0.6 on 2022-07-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_qualitydata_checkbeginn_qualitydata_checkend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitydata',
            name='failureStation',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]