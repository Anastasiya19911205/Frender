# Generated by Django 4.1.7 on 2023-05-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arrangement', '0012_establishments_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='status',
            field=models.CharField(choices=[('a', 'available'), ('b', 'busy')], default='a', max_length=1),
        ),
    ]
