# Generated by Django 2.0.8 on 2018-08-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0004_remove_artwork_artwork_year_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='artwork_yyyy_b',
            field=models.IntegerField(default=1900),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artwork_prid_a',
            field=models.IntegerField(default=0, verbose_name='PR ID - A'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artwork_prid_b',
            field=models.IntegerField(default=0, verbose_name='PR ID - B'),
        ),
    ]
