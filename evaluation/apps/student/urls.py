from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^addstudent/', views.add_student, name='add_student'),
]
