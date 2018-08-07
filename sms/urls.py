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
from rest_framework.routers import DefaultRouter
from django.urls import path


router=DefaultRouter()


from classe.models import *
from classe import views
router.register(r'classe',views.classeViewsets)

from section.models import *
from section import views
router.register(r'section',views.sectionViewsets)

from teacher.models import *
from teacher import views
router.register(r'teacher',views.teacherViewsets)

from student.models import *
from student import views
router.register(r'student',views.studentViewsets)


from library.models import *
from library import views
router.register(r'Librarie',views.LibrarieViewsets)

from parent.models import *
from parent import views
router.register(r'Parent',views.ParentViewsets)



from subject.models import *
from subject import views
router.register(r'Subject',views.SubjectViewsets)



from exam.models import *
from exam import views
router.register(r'Exam',views.ExamViewsets)



from attendence.models import *
from attendence import views
router.register(r'Attendence',views.AttendenceViewsets)



from accounting.models import *
from accounting import views
router.register(r'Accounting',views.AccountingViewsets)



from timetable.models import *
from timetable import views
router.register(r'timetable',views.timetableViewsets)


from newroom.models import *
from newroom import views
router.register(r'newroom',views.newroomViewsets)

from noticeboard.models import *
from noticeboard import views
router.register(r'noticeboard',views.noticeboardViewsets)



from calander.models import *
from calander import views
router.register(r'calander',views.CalanderViewsets)



























urlpatterns = [
   
    url(r'^',include(router.urls)),
	   path(('admin/'),admin.site.urls),
       
	
]
