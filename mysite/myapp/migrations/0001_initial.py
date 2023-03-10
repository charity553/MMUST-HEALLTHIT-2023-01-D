# Generated by Django 4.0.1 on 2023-01-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('area_name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Triage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=3)),
                ('blood_pressure', models.CharField(max_length=3)),
                ('respiratory_rate', models.CharField(max_length=3)),
                ('pulse_rate', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=3)),
                ('height', models.CharField(max_length=3)),
            ],
        ),
    ]
