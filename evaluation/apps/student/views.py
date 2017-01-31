from django.shortcuts import render
from django import forms
from .forms import StudentForm

# Create your views here.


def add_student(request):
    if request.method == 'GET':
        form = StudentForm()
    else:
        form = StudentForm(request.POST)

    # import ipdb; ipdb.set_trace()

    if form.is_valid():
        pass

    return render(request, 'base.html', {'form': form})
