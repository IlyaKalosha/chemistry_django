# Generated by Django 3.0.7 on 2021-12-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_agreed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
