# Generated by Django 3.0.8 on 2021-04-06 07:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201104_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2021)], verbose_name='Release year'),
        ),
    ]
