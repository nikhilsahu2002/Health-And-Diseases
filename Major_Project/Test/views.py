from django.shortcuts import render
from .models import persion
# Create your views here.
def home(request):
    data =persion.get()
    return render(request,'index.html',{'data':data})