from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse, reverse_lazy
from .forms import StudentForm, AltStudentForm
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


class CreateStudent(CreateView):
    template_name = 'base.html'
    model = Student
    fields = ('name', 'standard', 'marks')


class InsertStudent(FormView):
    template_name = 'base.html'
    form_class = AltStudentForm
    # success_url = '/insertstudent'
    success_url = reverse_lazy('student:insert_student')

    def form_valid(self, form):
        form.save_student()
        return super(InsertStudent, self).form_valid(form)
