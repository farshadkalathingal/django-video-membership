# Generated by Django 3.1.1 on 2020-09-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.IntegerField(default=150),
        ),
    ]
