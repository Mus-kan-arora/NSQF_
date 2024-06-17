# from .models import Faculty
# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# # Register your models here.
# # admin.site.register(TP,ImportExportModelAdmin)
# class FacultyAdmin(ImportExportModelAdmin):
#     # list_display=['id','Cat','Batch_Code','Roll_No']
#     list_per_page = 50
#     list_display=['user','coursename','centername']
# admin.site.register(Faculty,FacultyAdmin)



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import SimpleUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = SimpleUserCreationForm
    model = CustomUser

    list_display = ['username', 'email', 'first_name', 'last_name', 'course_name', 'center_name', 'user_date', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('course_name', 'center_name', 'user_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('course_name', 'center_name', 'user_date' )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
