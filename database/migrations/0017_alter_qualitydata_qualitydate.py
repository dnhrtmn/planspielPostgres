# Generated by Django 4.0.6 on 2022-07-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_rename_quality_qualitydata_failure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitydata',
            name='qualityDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
