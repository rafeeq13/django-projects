from django.contrib import admin

# Register your models here.
from .models import Contact_us,OpenadmissionModel,ApplicatoinModel

#regiser message form model
@admin.register (Contact_us)
class Contact_usAdmin(admin.ModelAdmin):
    list_display=['id','email','ph_no','message']


#register open admission form model

@admin.register(OpenadmissionModel)
class OpenadmissionModelAdmin(admin.ModelAdmin):
    list_display=['id','session','course','desc','fee','last_date']

#application madoel registeration
@admin.register(ApplicatoinModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=['name','dob','email','mobile','last_degree','course','gender','address']