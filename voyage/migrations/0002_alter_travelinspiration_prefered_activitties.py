# Generated by Django 4.2 on 2023-04-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelinspiration',
            name='prefered_activitties',
            field=models.CharField(max_length=500, verbose_name='prefered_activitties'),
        ),
    ]