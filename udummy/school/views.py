from django.shortcuts import render,HttpResponseRedirect
from .forms import Contact_form,Admissionopenform,ApplicatoinForm
from django.views import View
from .models import Contact_us ,OpenadmissionModel,ApplicatoinModel
from django.contrib import messages
from .forms import Signup,ChangeProfile
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.





# message POSt Method
def contact(request):

    if request.method=='POST':
        fm= Contact_form(request.POST)
        if fm.is_valid():
            fm.save()
    fm= Contact_form()
    st=OpenadmissionModel.objects.all()
    return render(request,'school/home.html',{'form':fm,'fm':st})

#message get method in another html template
def message_display(request):
    if not request.user.is_authenticated:
        fm=Contact_us.objects.all()
        st=ApplicatoinModel.objects.all()
        return render(request,'school/message.html',{'form':fm,'fm':st})
    return HttpResponseRedirect('/login/')


# message opened admissions

def openadmission(request):
    if request.method=="POST":
        fm=Admissionopenform(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Admissionopenform()

    fm=Admissionopenform()
    
    return render(request,'school/openadmission.html',{'form':fm})


#
#application form

def application(request):
    if request.user.is_authenticate:
        if not request.user.is_authenticated:
            if request.method=="POST":
                fm=ApplicatoinForm(request.POST)
                if fm.is_valid():
                    fm.save()
                    fm=ApplicatoinForm()
            else:
                fm=ApplicatoinForm()
            return render(request,'school/application.html',{'form':fm})
        return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/signup/')




#sign up form views

def signup(request):
    
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=Signup(request.POST)
            if fm.is_valid():
                fm.save()
                fm=Signup()
                messages.success(request,'Registered Successfully!')
                return HttpResponseRedirect('/login/')
        else:
            fm=Signup()
        return render(request,'school/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

    #login form 

def user_login(request):
    if not request.user.is_authenticated:

        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pwd=fm.cleaned_data['password']
                user=authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request, 'school/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


#user logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#user-change password
def change2(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'school/changepassword.html',{'form':fm})
    return HttpResponseRedirect('/login/')