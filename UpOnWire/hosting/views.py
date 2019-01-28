from django.shortcuts import render
from django.http import HttpResponse
from .forms import SetupForm
from .forms import UploadFileForm
from django.utils import timezone
from .fileHandler import uploadFileHandler
from .utils import randomIdGenerator

# Create your views here.
def index(request):
    if request.method == "POST":
        form = SetupForm(request.POST, request.FILES)
        uploadForm = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            setup = form.save(commit=False)
            setup.active = True
            setup.creationDate = timezone.now()
            hashId = randomIdGenerator
            setup.save()
            uploadFileHandler(request.FILES['file'], hashId)
            submitSuccessfully = True
            context = {
            'form': form,
            'submitSuccessfully': submitSuccessfully,
            'uploadForm':uploadForm
            }
            print(context)
            return render(request, 'hosting/index.html', {'context': context})
    else:
        form = SetupForm()
        uploadForm = UploadFileForm()
        submitSuccessfully = False
        context = {
        'form': form,
        'submitSuccessfully': submitSuccessfully,
        'uploadForm':uploadForm
        }
        return render(request, 'hosting/index.html', {'context': context})
