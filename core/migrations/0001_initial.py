# Generated by Django 3.0.7 on 2021-12-05 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('patronymic', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.FloatField()),
                ('reg_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('category', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('barcode', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(max_length=256)),
                ('expire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('pharmacy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pharmacy')),
                ('pill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pill')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('patronymic', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Manager')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pill',
            name='recipe_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Recipe'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pharmacy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pharmacy')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='pharmacy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pharmacy'),
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
                ('pill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pill')),
            ],
        ),
    ]
