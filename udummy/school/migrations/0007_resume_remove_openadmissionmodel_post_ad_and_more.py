# Generated by Django 4.2 on 2023-06-03 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_openadmissionmodel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('dob', models.DateTimeField()),
                ('gender', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Python Programming Language', 'Python Programming Language'), ('Mysql', 'Mysql'), ('Excel', '\t\tExcel'), ('SQL', '\t\tSQl'), ('WordPress', 'Wordpress'), ('Graphics Designing', 'Graphics Designing'), ('Full Stack Developer', 'Full Stack Developer'), ('ML', 'ML'), ('FLASK\t', '\tFLASK'), ('PYSRCIPT\t', '\tPYSCRIP'), ('\tJAVA\t', 'JAVA'), ('AI\t', '\tAI')], max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('st_class', models.CharField(max_length=70)),
                ('profile_image', models.ImageField(blank=True, upload_to='myimage')),
            ],
        ),
        migrations.RemoveField(
            model_name='openadmissionmodel',
            name='post_ad',
        ),
        migrations.AlterField(
            model_name='openadmissionmodel',
            name='course',
            field=models.CharField(choices=[('Python Programming Language', 'Python Programming Language'), ('Mysql', 'Mysql'), ('Excel', '\t\tExcel'), ('SQL', '\t\tSQl'), ('WordPress', 'Wordpress'), ('Graphics Designing', 'Graphics Designing'), ('Full Stack Developer', 'Full Stack Developer'), ('ML', 'ML'), ('FLASK\t', '\tFLASK'), ('PYSRCIPT\t', '\tPYSCRIP'), ('\tJAVA\t', 'JAVA'), ('AI\t', '\tAI')], max_length=50),
        ),
        migrations.AlterField(
            model_name='openadmissionmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='openadmissionmodel',
            name='session',
            field=models.CharField(choices=[('3 Months', '3 Months'), ('6 Months', '6 Months'), ('1 Year', '1 Year'), ('1.6 Years', '1.6 Years'), ('2 Years', '2 Years'), ('2.6 Years', '2.6 Years'), ('3 Years\t', '3 Years'), ('3.6 Years\t', '3.6 Years'), ('4 Years\t', '4 Years')], max_length=100),
        ),
    ]
