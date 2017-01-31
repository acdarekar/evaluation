from django.shortcuts import render, redirect
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
            redirect('/addstudent')

    return render(request, 'base.html', {'form': form, 'student_data': student_data})
