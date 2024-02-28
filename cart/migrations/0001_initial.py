# Generated by Django 5.0.1 on 2024-02-20 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bakery', '0008_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telephone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('unit_number', models.CharField(max_length=15)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('cake', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bakery.cakes')),
                ('pastry', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bakery.pastries')),
            ],
        ),
    ]
