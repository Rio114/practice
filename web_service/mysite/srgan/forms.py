from django import forms
from django.core.validators import FileExtensionValidator
from .models import FileNameModel

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = FileNameModel
#         fields = ['file_name', 'upload_time']

# class UploadFileForm(forms.Form):
#     # image data
#     original_name = forms.CharField(max_length=200)
#     hashed_name = forms.CharField(max_length=200)
