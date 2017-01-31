from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
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
            try:
                float(form.cleaned_data['marks'])
            except ValueError as e:
                error = 'You entered invalid value for Marks'
                return render(request, 'base.html', {'error': error, 'student_data': student_data})
            else:
                pass
            finally:
                pass
            form.save()
            redirect('/addstudent')

    return render(request, 'base.html', {'form': form, 'student_data': student_data})
