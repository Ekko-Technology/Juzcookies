# Generated by Django 5.0.1 on 2024-02-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0005_cakes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakes',
            name='sold_out',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastries',
            name='sold_out',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
