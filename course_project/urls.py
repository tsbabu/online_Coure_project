"""course_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #admin urls
    path('',views.index),
    path('admin-login/',views.adlogin,name='admin-login'),
    path('schedule_class/',views.schedule_class,name='schedule_class'),
    path('save/',views.save,name='save'),
    path('viewall_schedules/',views.viewall_schedules,name='viewall_schedules'),
    path('update_course/',views.update_course,name='update_course'),
    path('course_update/',views.course_update,name='course_update'),
    path('delete_course/',views.delete_course,name='delete_course'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('course_view/',views.course_view,name='course_view'),
    #student urls
    path('student/',views.Student,name='student'),

    path('student_register/',views.student_register,name='student_register'
    ),
    path('save_student_data/',views.save_student_data,name='save_student_data'),
    path('login_student/',views.login_student,name='login_student'),
    path('student_logincheck/',views.student_login_check,name='student_logincheck'),
    path('student_enroll/',views.student_enroll,name='student_enroll'),
    path('welcome_student/',views.welcome_student,name='welcome_student'),
    path('enroll_course/',views.enroll_course,name='enroll_course'),
    path('student_logout/',views.student_logout,name='student_logout'),
    path('view_enroll/',views.view_enroll,name='view_enroll'),
    path('cencel_enroll/',views.cencel_enroll,name='cencel_enroll'),
    path('searcphone/',views.searcphone,name='searcphone'),
    path('searchemail/',views.searchemail,name='searchemail')
]

