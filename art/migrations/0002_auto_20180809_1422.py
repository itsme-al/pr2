# Generated by Django 2.0.8 on 2018-08-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='artwork_yyyy_a',
            field=models.IntegerField(default=1900, max_length=4),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artwork_prid_a',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artwork_prid_b',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]