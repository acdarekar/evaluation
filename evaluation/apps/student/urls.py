from django.conf.urls import url

from . import views

app_name = 'student'
urlpatterns = [
    url(r'^addstudent/', views.add_student, name='add_student'),
    url(r'^createstudent/', views.CreateStudent.as_view(), name='create_student'),
    url(r'^insertstudent/', views.InsertStudent.as_view(), name='insert_student'),
    url(r'^putstudent/', views.PutStudent.as_view(), name='put_student'),
]
