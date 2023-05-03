from django.shortcuts import render
from .models import dataset
from django.db.models import Q
from .form import DiseaseFinderForm
# Create your views here.
def home(request):
    data = dataset.objects.filter(Q(Symptom_1__icontains="fever") | Q(Symptom_2__icontains="fever") | Q(Symptom_3__icontains="fever"))
    return render(request,'index.html',{'data':data})


def disease_finder(request):
    if request.method == 'POST':
        form = DiseaseFinderForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            q_objects = Q()
            for symptom in symptoms:
                q_objects |= Q(**{'{}__icontains'.format(symptom): 'Yes'})
            diseases = dataset.objects.filter(q_objects).values_list('Disease', flat=True)
            return render(request, 'result.html', {'diseases': diseases})
    else:
        form = DiseaseFinderForm()
    return render(request, 'index.html', {'form': form})