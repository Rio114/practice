import time
import sys, os

from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from .models import FileNameModel
from .get import get_image

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        return render(request, 'srgan/form.html')

    file = request.FILES['file']
    path = os.path.join(UPLOADE_DIR, file.name)
    destination = open(path, 'wb')

    for chunk in file.chunks():
        destination.write(chunk)

    get_image(file.name)

    insert_data = FileNameModel(file_name = file.name)
    insert_data.save()

    return redirect('srgan:complete')

def complete(request):
    return render(request, 'srgan/complete.html')

# class IndexView(generic.TemplateView):
#     template_name = 'srgan/index.html'

# class SendView(generic.TemplateView):

#     def post(self, request, *args, **kwargs):
#         context = {
#             'message': request.POST['message'],
#         }
#         return render(request, 'srgan/send.html', context)

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         print(form.is_valid())
#         print('-'*20)
#         print(form)
#         print('-'*20)
#         if form.is_valid():
#             # file is saved
#             form.save()
#             return HttpResponseRedirect('srgan:send')
#     else:
#         form = UploadFileForm()
#     return render(request, 'srgan/send.html', {'message': 'not good'})


# class MyFormView(View):
#     form_class = MyForm
#     initial = {'key': 'value'}
#     template_name = 'form_template.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#            # <process form cleaned data>
#            return redirect('/success/')
#         return render(request, self.template_name, {'form': form})