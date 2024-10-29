# medicines/views.py

from django.shortcuts import render
from .forms import MedicineSearchForm
from .models import Medicine

def home(request):
    form = MedicineSearchForm()
    return render(request, 'medicines/home.html', {'form': form})

def search(request):
    if request.method == 'POST':
        form = MedicineSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            components = form.cleaned_data['components']
            medicines = Medicine.objects.filter(components__icontains=components)
            alternatives = []

            for medicine in medicines:
                alternatives += list(medicine.alternatives.all())

            return render(request, 'medicines/results.html', {
                'medicines': medicines,
                'alternatives': alternatives,
                'name': name
            })
    else:
        form = MedicineSearchForm()
    return render(request, 'medicines/home.html', {'form': form})
