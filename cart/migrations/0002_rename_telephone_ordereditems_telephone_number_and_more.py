# Generated by Django 5.0.1 on 2024-02-20 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditems',
            old_name='telephone',
            new_name='telephone_number',
        ),
        migrations.AlterField(
            model_name='ordereditems',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='ordereditems',
            name='unit_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
