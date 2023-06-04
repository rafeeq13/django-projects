from django.db import models

# Create your models here.
class Contact_us(models.Model):
    email=models.EmailField(max_length=70)
    ph_no=models.PositiveIntegerField()
    message=models.TextField(max_length=252)


STATE_CHOICES=(
    ('3 Months'	,	'3 Months'),
    ('6 Months','6 Months'),
    ('1 Year','1 Year'),
    ('1.6 Years','1.6 Years'),
    ('2 Years','2 Years'),
    ('2.6 Years','2.6 Years'),
    ('3 Years	','3 Years'),
    ('3.6 Years	','3.6 Years'),
    ('4 Years	','4 Years')
)

COURSES_CHOICE=(
    ('Python Programming Language'	,	'Python Programming Language'),
    ('Mysql','Mysql'),
    ('Excel','		Excel'),
    ('SQL','		SQl'),
    ('WordPress','Wordpress'),
    ('Graphics Designing','Graphics Designing'),
    ('Full Stack Developer','Full Stack Developer'),
    ('ML','ML'),
    ('FLASK	','	FLASK'),
    ('PYSRCIPT	','	PYSCRIP'),
    ('	JAVA	','JAVA'),
    ('AI	','	AI')
)

class OpenadmissionModel(models.Model):
    session=models.CharField (choices=STATE_CHOICES,max_length=100)
    course=models.CharField(choices= COURSES_CHOICE,max_length=50)
    desc=models.CharField(max_length=252)
    fee=models.PositiveIntegerField()
    last_date=models.IntegerField()







LAST_DEGREE=(
    ('Intermediate','Intermediate'),
    ('Matric','Matric'),
    ('Bachelor','Bachelor'),
    ('Master','Matster'),
    ('PHD','PHD')
)

class ApplicatoinModel(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField(max_length=90)
    mobile=models.PositiveIntegerField()
    last_degree=models.CharField(max_length=100,choices=LAST_DEGREE)
    course=models.CharField(choices= COURSES_CHOICE,max_length=50)
    dob=models.DateTimeField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    
    
    