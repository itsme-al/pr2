# Generated by Django 2.0.8 on 2018-08-11 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0014_auto_20180810_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='name',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('C1', 'Consignments 1'), ('S1', 'Slides 1')], max_length=40, null=True, verbose_name='Name'),
        ),
    ]