from django.contrib import admin

# Register your models here.
from .models import Image_uploader

@admin.register(Image_uploader)
class Image_uploader(admin.ModelAdmin):
    list_display=['id','image','date']