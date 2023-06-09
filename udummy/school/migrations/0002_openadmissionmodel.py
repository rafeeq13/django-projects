# Generated by Django 4.2 on 2023-06-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenadmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.DateField()),
                ('course', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=252)),
                ('fee', models.PositiveIntegerField()),
                ('last_date', models.DateField()),
            ],
        ),
    ]
