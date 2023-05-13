# Generated by Django 4.1.7 on 2023-05-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0014_rename_max_spent_value_host_max_spend_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishments',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo_establishments'),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo_user'),
        ),
    ]
