# Generated by Django 2.1.7 on 2019-03-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='attractions',
            field=models.ManyToManyField(to='attractions.Attractions'),
        ),
    ]
