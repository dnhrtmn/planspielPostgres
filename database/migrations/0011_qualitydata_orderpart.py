# Generated by Django 4.0.6 on 2022-07-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_alter_qualitydata_ordernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualitydata',
            name='orderPart',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]