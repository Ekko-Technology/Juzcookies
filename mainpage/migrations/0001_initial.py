# Generated by Django 5.0.1 on 2024-02-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='mainpage/aboutuspics')),
                ('url', models.URLField()),
            ],
        ),
    ]
