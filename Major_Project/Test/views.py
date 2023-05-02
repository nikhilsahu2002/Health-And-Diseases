from django.shortcuts import render
from .models import dataset
# Create your views here.
def home(request):
    data = dataset.objects.all().filter('Fungal infection')
    return render(request,'index.html',{'data':data})