from django.contrib import admin

# Register your models here.
from .models import Resume
@admin.register(Resume)
class RsumeAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','gender','locality','city','zip_code',
                  'state','mobile','email',
                  'job_city','profile_image','my_file']