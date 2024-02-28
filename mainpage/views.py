from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CoverPic, ReviewPic 

# Create your views here.
def home(request):
    pictures = CoverPic.objects.all()
    reviews = ReviewPic.objects.all()
    return render(request, 'main.html', {'pictures': pictures, 'reviews': reviews})

def contact(request):
    return render(request,'contact.html')