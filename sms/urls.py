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
from rest_framework_bulk.routes import BulkRouter


router=BulkRouter()




from classe.models import *
from classe import views as classviews


from section.models import *
from section import views as sectionviews


from teacher.models import *
from teacher import views as teacherviews


from student.models import *
from student import views as studentviews


from library.models import *
from library import views as libraryviews

from parent.models import *
from parent import views as parentviews


from attendence.models import *
from attendence import views as attendenceviews

from subject.models import *
from subject import views as subjectviews



from exam.models import *
from exam import views as examviews
 


from exam.models import *
from exam import views as examviews


from settings.models import Institution,Academics,Caste_Religion
from settings import views as settingsviews
#router.register(r'Accounting',views.AccountingViewsets)



from timetable.models import *
from timetable import views as timetableviews


from newroom.models import *

from newroom import views as newroomviews

from noticeboard.models import *
from noticeboard import views as noticeboardviews



from calander.models import *
from calander import views as calanderviews

from rest_framework import urls

from book.models import *
from book import views as bookviews


from accounting.models import *
from accounting import views as accountingviews

from exam.models import *
from exam import views as examviews

from payment.models import *
from payment import views as paymentviews

from expense.models import *
from expense import views as expenseviews


from transport.models import *
from transport import views as transportviews


    
  
###path('settings/institution/<int:pk>/',settingsviews.Institutiondetails),
    


urlpatterns = [

    url(r'^',include(router.urls)),
    path(('admin/'),admin.site.urls),
    url(r'^transport/$',transportviews.transportList.as_view()),
    url(r'^transport/(?P<pk>[0-9]+)/$',transportviews.transportDetail.as_view()),
    url(r'^settings/castereligion/(?P<pk>[0-9]+)/$',settingsviews.CRdetails),
    url(r'^settings/castereligion/$',settingsviews.CRdetails),
    url(r'^settings/academics/(?P<pk>[0-9]+)/$',settingsviews.Academicsdetails),
    url(r'^settings/academics/$',settingsviews.Academicsdetails),
    url(r'^settings/institution/(?P<pk>[0-9]+)/$',settingsviews.Institutiondetails),
    url(r'^settings/institution',settingsviews.Institutiondetails),
    url(r'^book/$', bookviews.bookList.as_view()),
    url(r'^book/(?P<pk>[0-9]+)/$', bookviews.bookDetail.as_view()),
    url(r'^accounting/$', accountingviews.accountingList.as_view()),
    url(r'^accounting/(?P<pk>[0-9]+)/$', accountingviews.accountingDetail.as_view()),
    url(r'^attendence/$',attendenceviews.attendenceList.as_view()),
    url(r'^attendence/(?P<pk>[0-9]+)/$',attendenceviews.attendenceDetail.as_view()),
    url(r'^exam/$',examviews.examList.as_view()),
    url(r'^exam/(?P<pk>[0-9]+)/$',examviews.examDetail.as_view()),
    url(r'^parent/$',parentviews.parentList.as_view()),
    url(r'^parent/(?P<pk>[0-9]+)/$',parentviews.parentDetail.as_view()),
    url(r'^calander/$',calanderviews.calanderList.as_view()),
    url(r'^calander/(?P<pk>[0-9]+)/$',calanderviews.calanderDetail.as_view()),
    url(r'^classe/$',classviews.classeList.as_view()),
    url(r'^classe/(?P<pk>[0-9]+)/$',classviews.classeDetail.as_view()),
    url(r'^section/$',sectionviews.sectionList.as_view()),
    url(r'^section/(?P<pk>[0-9]+)/$',sectionviews.sectionDetail.as_view()),
    url(r'^student/$',studentviews.studentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)/$',studentviews.studentDetail.as_view()),
    url(r'^student/qualifications/$',studentviews.qualificationList.as_view()),
    url(r'^student/qualifications/(?P<pk>[0-9]+)/$',studentviews.qualificationDetail.as_view()),
    url(r'^student/admission/$',studentviews.admissionList.as_view()),
    url(r'^student/admission/(?P<pk>[0-9]+)/$',studentviews.admissionDetail.as_view()),
    url(r'^student/other/$',studentviews.otherList.as_view()),
    url(r'^student/other/(?P<pk>[0-9]+)/$',studentviews.otherDetail.as_view()), 
    url(r'^student/hostel/$',studentviews.hostelList.as_view()),
    url(r'^student/hostel/(?P<pk>[0-9]+)/$',studentviews.hostelDetail.as_view()),
    url(r'^teacher/$',teacherviews.teacherList.as_view()),
    url(r'^teacher/(?P<pk>[0-9]+)/$',teacherviews.teacherDetail.as_view()),
    url(r'^subject/$',subjectviews.subjectList.as_view()),
    url(r'^subject/(?P<pk>[0-9]+)/$',subjectviews.subjectDetail.as_view()),
    url(r'^timetable/$',timetableviews.timetableList.as_view()),
    url(r'^timetable/(?P<pk>[0-9]+)/$',timetableviews.timetableDetail.as_view()),
    url(r'^noticeboard/$',noticeboardviews.noticeboardList.as_view()),
    url(r'^noticeboard/(?P<pk>[0-9]+)/$',noticeboardviews.noticeboardDetail.as_view()),
    url(r'^newroom/$',newroomviews.newroomList.as_view()),
    url(r'^newroom/(?P<pk>[0-9]+)/$',newroomviews.newroomDetail.as_view()),
    url(r'^payment/$',paymentviews.InvoiceList.as_view()),
    url(r'^payment/(?P<pk>[0-9]+)/$',paymentviews.InvoiceDetail.as_view()),
    url(r'^payment/$',paymentviews.MassInvoiceView.as_view()),
    url(r'^expense/$',expenseviews.ExpenseList.as_view()),
    url(r'^expense/(?P<pk>[0-9]+)/$',expenseviews.ExpenseDetail.as_view()),
    

]
