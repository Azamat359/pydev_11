from django.shortcuts import render,get_list_or_404
from . import models
def homepage(request):
    telefonlar=models.Mobi.objects.all()
    return render(request,'home.html',{'telefonlar':telefonlar})
def detail(request,id):
    telefon = get_list_or_404(models.Mobi,id=id)
    return render(request,'detail.html',{'telefon':telefon})   
# Create your views here.
