from django.shortcuts import render
from .models import Image_uploader
from .froms import  Image_form
# Create your views here.
def image_iplaoder(request):
    if request.method=="POST":
        fm=Image_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    fm=Image_form()
    img=Image_uploader.objects.all()
    return render (request,'enroll/home.html',{'form':fm,'fm':img})