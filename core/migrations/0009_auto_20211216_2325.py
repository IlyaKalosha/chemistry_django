# Generated by Django 3.0.7 on 2021-12-16 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211216_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='count',
            new_name='counter',
        ),
    ]
