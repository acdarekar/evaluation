from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import StudentForm
from .models import Student

# Create your views here.


def add_student(request):
    student_data = Student.objects.all()
    if request.method == 'GET':
        form = StudentForm()
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(reverse('student:add_student'))

    return render(request, 'base.html', {'form': form, 'student_data': student_data})
