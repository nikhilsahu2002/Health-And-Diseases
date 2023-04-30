from django.shortcuts import render
from . import mongo
# Create your views here.
def home(request):
    data =mongo.get_data()
    return render(request,'index.html')