# Generated by Django 4.0.2 on 2022-02-22 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WayPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='название')),
                ('latitude', models.CharField(max_length=6, verbose_name='широта')),
                ('longitude', models.CharField(max_length=6, verbose_name='долгота')),
            ],
        ),
    ]
