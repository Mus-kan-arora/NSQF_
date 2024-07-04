from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User
from employee.models import TP

from .models import *
from django.db.models import Func

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
#


# def internal_ass(request):
#     if not request.user.is_authenticated:
#         return redirect('login')

#     current_month = request.user.user_date.month
#     current_year = request.user.user_date.year

#     # Check for date consistency
#     try:
#         start_date = datetime(current_year, current_month, 1)
#         end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
#     except Exception as e:
#         return render(request, 'error.html', {'message': 'Date error'})

#     this_course = request.user.course_name
#     data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
#     items = data.filter(Course_Name=this_course)

#     user = request.user

#     section = request.GET.get('option')
#     print(f"Section: {section}")

#     if request.method == 'POST':
#         print("POST request received")

#         for item in items:
#             item_id = str(item.id)

#             if section == 'internal_table':
#                 if user.submitted_internal and user.submission_date_internal.month == current_month and user.submission_date_internal.year == current_year:
#                     if request.is_ajax():
#                         return JsonResponse({'error': 'Internal assessment already submitted for this month.'})
#                     return render(request, 'submitted.html')
#                 else:
#                     internal1 = request.POST.get(f'internal1_{item_id}', '0')
#                     internal2 = request.POST.get(f'internal2_{item_id}', '0')
#                     total_internal = request.POST.get(f'total_internal_{item_id}', '0')
#                     print(f"Internal: {internal1}, {internal2}, {total_internal}")

#                     item.IS1 = internal1
#                     item.IS2 = internal2
#                     item.Internal_Assessment = total_internal
#                     item.save()

#                     user.submitted_internal = True
#                     user.submission_date_internal = user.user_date
#                     user.save()

#             elif section == 'practical_table':
#                 if user.submitted_practical and user.submission_date_practical.month == current_month and user.submission_date_practical.year == current_year:
#                     if request.is_ajax():
#                         return JsonResponse({'error': 'Practical assessment already submitted for this month.'})
#                     return render(request, 'submitted.html')

#                 practical = request.POST.get(f'practical_{item_id}', '0')
#                 print(f"Practical: {practical}")

#                 item.Practical1 = practical
#                 item.save()

#                 user.submitted_practical = True
#                 user.submission_date_practical = user.user_date
#                 user.save()

#             elif section == 'assignment_table':
#                 if user.submitted_assignment and user.submission_date_assignment.month == current_month and user.submission_date_assignment.year == current_year:
#                     if request.is_ajax():
#                         return JsonResponse({'error': 'Assignment already submitted for this month.'})
#                     return render(request, 'submitted.html')
#                 else:
#                     assignment = request.POST.get(f'assignment_{item_id}', '0')
#                     print(f"Assignment: {assignment}")

#                     item.Project = assignment
#                     item.save()

#                     user.submitted_assignment = True
#                     user.submission_date_assignment = user.user_date
#                     user.save()

#         if request.is_ajax():
#             return JsonResponse({'success': 'Data submitted successfully!'})

#         return redirect('/internal_marks/')  # Redirect to a success page or reload the form

#     return render(request, 'updation.html', {'data': items, 'this_course': this_course, 'section': section})

def internal_ass(request):
    if not request.user.is_authenticated:
        messages.error(request, 'User not authenticated')
        return redirect('login')

    current_month = request.user.user_date.month
    current_year = request.user.user_date.year

    # Check for date consistency
    try:
        start_date = datetime(current_year, current_month, 1)
        end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
    except Exception as e:
        messages.error(request, 'Date error')
        return render(request, 'error.html', {'message': 'Date error'})

    this_course = request.user.course_name
    data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
    items = data.filter(Course_Name=this_course)

    user = request.user
    section = request.GET.get('option')
    print(f"Section: {section}")

    if request.method == 'POST':
        print("POST request received")
        for item in items:
            item_id = str(item.id)

            if section == 'internal_table':
                if user.submitted_internal and user.submission_date_internal.month == current_month and user.submission_date_internal.year == current_year:
                    messages.error(request, 'Internal assessment already submitted')
                    return redirect('/internal_marks/')
                else:
                    internal1 = request.POST.get(f'internal1_{item_id}', '0')
                    internal2 = request.POST.get(f'internal2_{item_id}', '0')
                    total_internal = request.POST.get(f'total_internal_{item_id}', '0')
                    print(f"Internal: {internal1}, {internal2}, {total_internal}")

                    item.IS1 = internal1
                    item.IS2 = internal2
                    item.Internal_Assessment = total_internal
                    item.save()

                    user.submitted_internal = True
                    user.submission_date_internal = user.user_date
                    user.save()

            elif section == 'practical_table':
                if user.submitted_practical and user.submission_date_practical.month == current_month and user.submission_date_practical.year == current_year:
                    messages.error(request, 'Practical assessment already submitted')
                    return redirect('/internal_marks/')

                practical = request.POST.get(f'practical_{item_id}', '0')
                print(f"Practical: {practical}")

                item.Practical1 = practical
                item.save()

                user.submitted_practical = True
                user.submission_date_practical = user.user_date
                user.save()

            elif section == 'assignment_table':
                if user.submitted_assignment and user.submission_date_assignment.month == current_month and user.submission_date_assignment.year == current_year:
                    messages.error(request, 'Assignment already submitted')
                    return redirect('/internal_marks/')
                else:
                    assignment = request.POST.get(f'assignment_{item_id}', '0')
                    print(f"Assignment: {assignment}")

                    item.Project = assignment
                    item.save()

                    user.submitted_assignment = True
                    user.submission_date_assignment = user.user_date
                    user.save()

        messages.success(request, 'Data successfully submitted')
        return redirect('/internal_marks/')

    return render(request, 'updation.html', {'data': items, 'this_course': this_course, 'section': section})
# def internal_ass(request):
#     if not request.user.is_authenticated:
#         return redirect('login')

#     current_month = request.user.user_date.month
#     current_year = request.user.user_date.year

#     # Check for date consistency
#     try:
#         start_date = datetime(current_year, current_month, 1)
#         end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)
#     except Exception as e:
#         return render(request, 'error.html', {'message': 'Date error'})

#     this_course = request.user.course_name
#     data = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
#     items = data.filter(Course_Name=this_course)

#     user = request.user


#     section = request.GET.get('option')
#     print(f"Section: {section}")

#     if request.method == 'POST':
#         print("POST request received")

#         for item in items:
#             item_id = str(item.id)

#             if section == 'internal_table':

#                 if user.submitted_internal and user.submission_date_internal.month == current_month and user.submission_date_internal.year == current_year :
#                     return render(request, 'submitted.html')
#                 else:
#                     internal1 = request.POST.get(f'internal1_{item_id}', '0')
#                     internal2 = request.POST.get(f'internal2_{item_id}', '0')
#                     total_internal = request.POST.get(f'total_internal_{item_id}', '0')
#                     print(f"Internal: {internal1}, {internal2}, {total_internal}")

#                     item.IS1 = internal1
#                     item.IS2 = internal2
#                     item.Internal_Assessment = total_internal
#                     item.save()

#                     user.submitted_internal = True
#                     user.submission_date_internal = user.user_date
#                     user.save()

#             elif section == 'practical_table':

#                 if user.submitted_practical and user.submission_date_practical.month == current_month and user.submission_date_practical.year == current_year :
#                     return render(request, 'submitted.html')

#                 practical = request.POST.get(f'practical_{item_id}', '0')
#                 print(f"Practical: {practical}")

#                 item.Practical1 = practical
#                 item.save()

#                 user.submitted_practical = True
#                 user.submission_date_practical = user.user_date
#                 user.save()

#             elif section == 'assignment_table':
#                 print(user.submitted_assignment)
#                 if user.submitted_assignment and user.submission_date_assignment.month == current_month and user.submission_date_assignment.year == current_year:
#                     return render(request, 'submitted.html')
#                 else:
#                     assignment = request.POST.get(f'assignment_{item_id}', '0')
#                     print(f"Assignment: {assignment}")

#                     item.Project = assignment
#                     item.save()

#                     user.submitted_assignment = True
#                     user.submission_date_assignment = user.user_date
#                     user.save()

#         return redirect('/internal_marks/')  # Redirect to a success page or reload the form

#     return render(request, 'updation.html', {'data': items, 'this_course': this_course, 'section': section})




def Logout_faculty(request):
    logout(request)
    return redirect('/')


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
    student_display = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
    students = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
    print(course)
    if course:
        student_display = students.filter(Course_Name__icontains=course)

    # Use distinct on the original field with order_by
    course_names = students.values_list('Course_Name', flat=True).order_by('Course_Name').distinct()

    print(f"Number of students after course filter: {students.count()}")
    context = {
        'course': course,
        'course_names': course_names,
        'students': student_display,
        'current_month': current_month,
        'current_year': current_year,
    }
    return render(request, 'attandance.html', context)



# def attandancedetail(request):
#     # Get the current month and year
#     course = request.GET.get('course_name')
#     current_month = request.user.user_date.month
#     current_year = request.user.user_date.year
#     # current_month = datetime.now().month
#     # current_year = datetime.now().year

#     # Calculate the start and end date of the current month
#     start_date = datetime(current_year, current_month, 1)
#     end_date = datetime(current_year, current_month + 1, 1) if current_month < 12 else datetime(current_year + 1, 1, 1)

#     # Filter the data from TP model based on the current month and year
#     student_display = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
#     students = TP.objects.filter(Date_of_Exam__gte=start_date, Date_of_Exam__lt=end_date).order_by('Name_of_the_Candidate')
#     print(course)
#     if course:
#         student_display = students.filter(Course_Name__icontains=course)
#     #course_names = students.filter().values_list('Course_Name', flat= True).distinct()
#     course_names = students.annotate(
#     clean_course_name=Func('Course_Name', function='LOWER')
# ).values_list('clean_course_name', flat=True).distinct()
#     print(f"Number of students after course filter: {students.count()}")
#     context = {
#         'course':course,
#         'course_names': course_names,
#         'students': student_display,
#         'current_month': current_month,
#         'current_year': current_year,
#     }
#     return render(request, 'attandance.html', context)




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

