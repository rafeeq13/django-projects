# Generated by Django 4.2 on 2023-06-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('ph_no', models.PositiveIntegerField()),
                ('message', models.TextField(max_length=252)),
            ],
        ),
    ]
