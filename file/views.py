from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

from django import forms

from file.models import IMG


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(image):
    path = default_storage.save('./images/'+image.name,ContentFile(image.read()))


def upload_file(request):

    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('image'),
            name=request.FILES.get('image').name
        )
        new_img.save()
        return HttpResponse('Success!')
    else:
        return HttpResponse('Not a post!')
