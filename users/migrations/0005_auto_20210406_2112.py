# Generated by Django 3.0.8 on 2021-04-06 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210406_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username']},
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(max_length=1000, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='user', max_length=50, verbose_name='Уровень доступа'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Псевдоним'),
        ),
    ]
