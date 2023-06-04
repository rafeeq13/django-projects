from django.db import models

# Create your models here.c
STATE_CHOICES=(
    ('Bahawalpur'	,	'Bahawalpur'),
    ('Dera Ghazi Khan','Dera Ghazi Khan	'),
    ('Faisalabad','		Faisalabad'),
    ('Gujranwala','		Gujranwala'),
    ('Lahore','		Lahore'),
    ('Mianwali','Mianwali'),
    ('Multan	','Multan'),
    ('Rawalpindi	','	Rawalpindi'),
    ('Sahiwal	','	Sahiwal'),
    ('	Sargodha	','Sargodha'),
    ('Gujrat	','	Gujrat')
)

class Resume(models.Model):
    name=models.CharField(max_length=55)
    dob=models.DateTimeField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=20)
    locality=models.CharField(max_length=50)
    city=models.CharField(max_length=100)
    zip_code=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICES ,max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField(max_length=70)
    job_city=models.CharField(max_length=70)
    profile_image=models.ImageField(upload_to='myimage',blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)