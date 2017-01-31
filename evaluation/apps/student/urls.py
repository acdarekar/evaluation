from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addstudent/', views.add_student, name='add_student'),
    url(r'^createstudent/', views.CreateStudent.as_view(), name='create_student'),
]
