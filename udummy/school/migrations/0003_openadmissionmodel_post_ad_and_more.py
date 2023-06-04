# Generated by Django 4.2 on 2023-06-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_openadmissionmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='openadmissionmodel',
            name='post_ad',
            field=models.ImageField(default=False, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='openadmissionmodel',
            name='last_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='openadmissionmodel',
            name='session',
            field=models.IntegerField(),
        ),
    ]