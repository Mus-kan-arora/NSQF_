from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User
from employee.models import TP
from django.contrib import messages
from .models import *
# Create your views here.
# def faculty1(request):
#     if request.method == 'POST':
#         username = request.POST['email']
#         centercode = request.POST['centercode']
#         coursecode = request.POST['coursecode']
#         fname = request.POST['firstname']
#         lname=request.POST['lastname']
#         password = request.POST['pwd']
#         if User.objects.filter(username=username).exists():
#             messages.info(request, "Already used this email id.")
#         else:
#             # Create a user using Django's authentication system
#             user = User.objects.create_user(username=username, first_name=fname,last_name=lname, password=password)
#             coursecode=TP.objects.filter(Course_Name__icontains=coursecode).first()
#             # username=user.username
#              # Create Faculty object
#             Faculty.objects.create(user=user,coursename=coursecode, centername=centercode)
#             return redirect('/faculty_signup_data')
#     return render(request,'faculty_signup_data.html')

# def faculty_home(request):
#     return render(request,'faculty_home.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SimpleUserCreationForm
from employee.models import *
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime
from django.utils.timezone import now
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def create_non_staff_user(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            custom_user = form.save(commit=False)
            custom_user.is_staff = False
            custom_user.save()
            messages.success(request, 'Non-staff user created successfully!')
            # messages.success("Account Created successfully")
            return redirect('/faculty_signup_data/')
        else:
            messages.error(request, 'Something went wrong. Please correct the errors below.')
    else:
        form = SimpleUserCreationForm()
    return render(request, 'faculty_signup_data.html', {'form': form})




# def internal_ass(request):
#     this_course = request.user.course_name
#     section = request.GET.get('option')

#     if request.method == 'POST':
#         items = TP.objects.filter(Course_Name=this_course)

#         for item in items:
#             item_id = str(item.id)
#             if section == 'internal_table':
#                 internal1 = request.POST.get(f'internal1_{item_id}')
#                 internal2 = request.POST.get(f'internal2_{item_id}')
#                 total_internal = request.POST.get(f'total_internal_{item_id}')
#                 item.IS1 = internal1
#                 item.IS2 = internal2
#                 item.Internal_Assessment = total_internal
#                 item.save()

#             if section == 'practical_table':
#                 practical = request.POST.get(f'practical_{item_id}')
#                 item.Practical1 = practical
#                 item.save()

#             if section == 'assignment_table':
#                 assignment = request.POST.get(f'assignment_{item_id}')
#                 item.Project = assignment
#                 item.save()

#         # Redirect to a success page after processing POST data
#         return HttpResponseRedirect(reverse('internal_marks'))

#     else:
#         current_month = request.user.user_date.month
#         current_year = request.user.user_date.year
#         start_date = datetime(current_year, current_month, 1)
#         end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
#         data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
#         data = data.filter(Course_Name=this_course)

#         return render(request, 'updation.html', {'data': data, 'this_course': this_course, 'section': section})



# @login_required
def internal_ass(request):
    current_month = request.user.user_date.month
    current_year = request.user.user_date.year
    start_date = datetime(current_year, current_month, 1)
    end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
    this_course = request.user.course_name
    data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
    items = data.filter(Course_Name=this_course)

    section = request.GET.get('option')
    print(section)
    if request.method == 'POST':
        for item in items:
            item_id = str(item.id)
            if section == 'internal_table':
                internal1 = request.POST.get(f'internal1_{item_id}', '0')
                internal2 = request.POST.get(f'internal2_{item_id}', '0')
                total_internal = request.POST.get(f'total_internal_{item_id}', '0')
                print(internal1, internal2, total_internal)
                item.IS1 = internal1
                item.IS2 = internal2
                item.Internal_Assessment = total_internal
                item.save()

            elif section == 'practical_table':
                practical = request.POST.get(f'practical_{item_id}')
                print(practical)
                item.Practical1 = practical
                item.save()

            elif section == 'assignment_table':
                assignment = request.POST.get(f'assignment_{item_id}')
                print(assignment)
                item.Project = assignment
                item.save()

        return redirect('/internal_marks/')  # Redirect to a success page or reload the form

    return render(request, 'updation.html', {'data': items, 'this_course': this_course, 'section': section})


# def internal_ass(request):
#     current_month = request.user.user_date.month
#     current_year = request.user.user_date.year
#     start_date = datetime(current_year, current_month, 1)
#     end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
#     this_course = request.user.course_name
#     data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
#     items = data.filter(Course_Name=this_course)

#     section = request.GET.get('option')
#     print(section)
#     if request.method == 'POST':

#         # internal1 = request.POST.get(f'internal1_{item_id}')

#         for item in items:
#             item_id = str(item.id)
#             if section == 'internal_table':
#                 internal1 = request.POST.get(f'internal1_{item_id}')
#                 internal2 = request.POST.get(f'internal2_{item_id}')
#                 total_internal = request.POST.get(f'total_internal_{item_id}')
#                 print(internal1)
#                 print(internal2)
#                 print(total_internal)
#                 item.IS1 = internal1
#                 item.IS2 = internal2
#                 item.Internal_Assessment = total_internal
#                 item.save()

#             if section == 'practical_table':
#                  practical = request.POST.get(f'practical_{item_id}')
#                  print(practical)
#                  item.Practical1 = practical
#                  item.save()

#             if section == 'assignment_table':
#                 assignment = request.POST.get(f'assignment_{item_id}')
#                 item.Project = assignment


#         response = redirect('/internal_marks/')  # Redirect to a success page or reload the form

#         return response

#     else:
#         # current_month = request.user.user_date.month
#         # current_year = request.user.user_date.year

#         # start_date = datetime(current_year, current_month, 1)
#         # end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
#         # data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')

#         # data = data.filter(Course_Name=this_course)


#         return render(request, 'updation.html', {'data': items, 'this_course': this_course, 'section':section})



       # form_submitted = request.session.get('form_submitted', False)
        # if form_submitted:
        #     messages.info(request, 'Form has already been submitted.')
        # # print(data)
        # # for item in data:
        # #     print(f"ID: {item.id}, Roll No: {item.Roll_No}, Internal 1: {item.IS1}")
        # return render(request, 'internal_updation.html', {'data': data, 'this_course':this_course})


# def internal_ass(request):
#     this_course = request.user.course_name
#     if request.method == 'GET':
#         batch = request.GET.get('batch')
#         option = request.GET.get('option')
#         print(option)

#         if option:
#             batch_objects = TP.objects.filter(Course_Name=this_course, Batch_Code=batch)
#             context = {
#                 'data': batch_objects,
#                 'option': option,
#                 'this_course': this_course,
#                 'batches': TP.objects.filter(Course_Name=this_course).values_list('Batch_Code', flat=True).distinct()
#             }
#             return render(request, 'internal_updation.html', context)
#     else:
#         distinct_batches = TP.objects.filter(Course_Name=this_course).values_list('Batch_Code', flat=True).distinct()
#         context = {
#             'batches': distinct_batches,
#             'this_course': this_course
#         }
#         return render(request, 'internal_updation.html', context)



def attandancedetail(request):
    # Get the current month and year
    course = request.GET.get('course_name')
    current_month = request.user.user_date.month
    current_year = request.user.user_date.year
    # current_month = datetime.now().month
    # current_year = datetime.now().year

    # Calculate the start and end date of the current month
    start_date = datetime(current_year, current_month, 1)
    end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)

    # Filter the data from TP model based on the current month and year
    students = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
    print(course)
    if course:
        students = students.filter(Course_Name__icontains=course)
    course_names = TP.objects.filter().values_list('Course_Name', flat= True).distinct()
    print(f"Number of students after course filter: {students.count()}")
    context = {
        'course':course,
        'course_names': course_names,
        'students': students,
        'current_month': current_month,
        'current_year': current_year,
    }
    return render(request, 'attandance.html', context)




def faculty_save_data(request):
    if request.method == 'POST':
        field1 = request.POST.get('internal1')
        field2 = request.POST.get('internal2')
        field3 = request.POST.get('total_internal')
        print(field3)
        obj_id = request.POST.get('id')
        try:
            obj = TP.objects.get(pk=obj_id)
            obj.IS1 = field1
            obj.IS2 = field2
            obj.Internal_Assessment = field3
            obj.save()
            return JsonResponse({'success': True})
        except TP.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object not found'})
        except Exception as e:
            print("Error occurred while saving data:", e)
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def faculty_save_practical_data(request):
    if request.method == 'POST':
        field1 = request.POST.get('practical')
        obj_id = request.POST.get('id')
        try:
            obj = TP.objects.get(pk=obj_id)
            obj.Practical1 = field1
            obj.save()
            return JsonResponse({'success': True})
        except TP.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object not found'})
        except Exception as e:
            print("Error occurred while saving data:", e)
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def faculty_save_assignment_data(request):
    if request.method == 'POST':
        field1 = request.POST.get('assignment')
        obj_id = request.POST.get('id')
        try:
            obj = TP.objects.get(pk=obj_id)
            obj.Project = field1
            obj.save()
            return JsonResponse({'success': True})
        except TP.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Object not found'})
        except Exception as e:
            print("Error occurred while saving data:", e)
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

