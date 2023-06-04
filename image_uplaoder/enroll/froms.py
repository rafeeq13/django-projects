from django import forms

from .models import Image_uploader

class Image_form(forms.ModelForm):
    class Meta:
        model=Image_uploader
        fields=('__all__')
        labels={'image':''}