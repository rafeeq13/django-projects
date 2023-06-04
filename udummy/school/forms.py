from django import forms
from .models import Contact_us,OpenadmissionModel,ApplicatoinModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

#Conact message for 
class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact_us
        fields='__all__'
        labels={
            'ph_no':'Phone No'
        }
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'ph_no':forms.NumberInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'})
        }


#admssion open form 

class Admissionopenform(forms.ModelForm):
    class Meta:
        model=OpenadmissionModel
        fields='__all__'
        labels={
            'session':'Course Duration','course':'Course Name',
            'desc':'Course Details','fee':'Course fee','last_date':'Last Date'
        }
        widgets={
            
            'desc':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your program details'}),
            'fee':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your fee'}),
            'last_date':forms.NumberInput(attrs={'class':'form-control','placeholder':'XX'})
            
        }



#application Form
GENER_CHOICES=[
    ('male','male'),
    ('female','female')
]
class ApplicatoinForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model=ApplicatoinModel
        fields='__all__'
        labels={
            'name':'Full Name','dob':'Date Of Birth','address':'Permanent Address','course':'Applying for'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),

        }


#sign up form 
class Signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'}),
        'password2':forms.PasswordInput(attrs={'class':'form-control'}),

    }



#change profile
class ChangeProfile(UserChangeForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']


#sign up form
from django.contrib.auth.forms import UserCreationForm
class Signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']