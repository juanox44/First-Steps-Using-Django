# Generated by Django 4.0.4 on 2022-05-01 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('species', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
