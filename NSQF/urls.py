from django.contrib import admin
from django.urls import path,include
from employee.views import *
from faculty.views import *
from django.conf import settings # new
from  django.conf.urls.static import static #new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', save_data, name='save_data'),
    path('download_report/',download_report,name='download_report'),
    path('download_report_data/',download_report_data,name='download_report_data'),
    path('',index),
    path('logout/',Logout),
    path('admin_login',admin_login,name='admin_login'),
    path('admin_home',admin_home,name='admin_home'),
    path('change_passwordadmin',change_passwordadmin,name='change_passwordadmin'),
    path('all_employee',all_employee, name='all_employee'),
    path('all_employee_data',all_employee_data, name='all_employee_data'),
    path('display_data/',display_data,name='display_data'),
    path('display_data_data/',display_data_data,name='display_data_data'),
    path('nielitheader/',nielitheader,name='nielitheader'),
    path('faculty_signup_data/',create_non_staff_user,name='faculty_signup_data'),
    path('faculty_home/',faculty_home,name='faculty_home'),
    path('attandance/', attandancedetail, name= 'attandancedetail' ),
    path('internal_marks/', internal_ass, name = 'internal_ass'),
    path('faculty_save/', faculty_save_data, name ='faculty_save_data'),
     path('admin-view-course/<str:course_name>/', view_course, name='admin_view_course'),
    path('faculty_save_practical/', faculty_save_practical_data, name='faculty_save_practical_data'),
    path('faculty_save_assignment/', faculty_save_assignment_data, name='faculty_save_practical_data'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
