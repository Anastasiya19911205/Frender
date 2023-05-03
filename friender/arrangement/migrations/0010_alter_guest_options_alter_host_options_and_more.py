# Generated by Django 4.1.7 on 2023-04-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0009_users_arrangement_age_d35502_idx_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name_plural': 'гости'},
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name_plural': 'приглашающие'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'пользователи', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='users',
            name='city',
            field=models.CharField(default='Minsk', max_length=100, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=100, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='users',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='фамилия'),
        ),
    ]
