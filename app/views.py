from django.shortcuts import render
from .models import AboutUs,Service


def home(request):
    service=Service.objects.only('image','title','description')
    aboutus=AboutUs.objects.only('image').last()
    context={
        'service':service,
        'about':aboutus
        }
    return render(request, 'home.html',context)


def about(request):
    aboutus=AboutUs.objects.only('image').last()
    context={
        'about':aboutus
        }
    return render(request, 'about.html',context)


def services(request):

    service=Service.objects.only('image','title','description')
    context={
        'service':service
        }
    return render(request, 'services.html',context)


def contact(request):
    return render(request, 'contact.html')


