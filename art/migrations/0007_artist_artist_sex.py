# Generated by Django 2.0.8 on 2018-08-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0006_auto_20180809_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N/A', 'N/A')], max_length=3, null=True),
        ),
    ]
