# Generated by Django 3.0.7 on 2021-12-08 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe_pill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Manager'),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Seller'),
        ),
    ]