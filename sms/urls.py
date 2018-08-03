"""sms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from eduinfosys import views
from rest_framework.routers import SimpleRouter
from django.urls import path
from eduinfosys.models import *
router=SimpleRouter()
router.register(r'classe',views.classeViewsets)
router.register(r'section',views.sectionViewsets)
router.register(r'teacher',views.teacherViewsets)
router.register(r'student',views.studentViewsets)
router.register(r'Librarie',views.LibrarieViewsets)
router.register(r'Parent',views.ParentViewsets)
router.register(r'Subject',views.SubjectViewsets)
router.register(r'Exam',views.ExamViewsets)
router.register(r'Attendence',views.AttendenceViewsets)
router.register(r'Accounting',views.AccountingViewsets)

urlpatterns = [
   
    url(r'^',include(router.urls)),
	   path(('admin/'),admin.site.urls),
	
]