from django.shortcuts import render, redirect
from .models import Dataset
from .forms import DatasetForm

def dataset_list(request):
    datasets = Dataset.objects.all()
    return render(request, 'dataset_list.html', {'datasets': datasets})

def dataset_create(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dataset_list')
    else:
        form = DatasetForm()
    return render(request, 'dataset_form.html', {'form': form})
