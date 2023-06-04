from .models import Resume
from django import forms


GENER_CHOICES=[
    ('male','male'),
    ('female','female')
]
CITY_CHOICES=(
    ('Bahawalpur'	,	'Bahawalpur'),
    ('Dera Ghazi Khan','Dera Ghazi Khan	'),
    ('Faisalabad','		Faisalabad'),
    ('Gujranwala','		Gujranwala'),
    ('Lahore','		Lahore')
)
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label='Prefered job location!',
                                       choices=CITY_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['id','name','dob','gender','locality','city','zip_code',
                  'state','mobile','email',
                  'job_city','profile_image','my_file']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zip_code':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
  


        }
